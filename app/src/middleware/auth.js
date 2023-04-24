import express from "express";
import dotenv from "dotenv";

if (process.env.RUN_FLAG === "dev") {
  dotenv.config({ path: ".devEnv" });
} else {
  dotenv.config();
}

import passport from "passport";
import * as passportAzureAd from "passport-azure-ad";
const { BearerStrategy } = passportAzureAd;
import jwt_decode from "jwt-decode";

const app = express();
app.use(passport.initialize()); // Starts passport

import { logInformationSendResponse } from "./logs.js";
import { dice_pool } from "../utils/dice_pool.js";

import {
  validateRBACPermissionForAction,
  validateUserInGroups,
} from "../routes/Validations/ValidationsFnComponents.js";

const creds = {
  // Requried
  identityMetadata: `https://login.microsoftonline.com/${process.env.AZURE_APP_TENANT_GUID}/v2.0/.well-known/openid-configuration`,
  // or 'https://login.microsoftonline.com/<your_tenant_guid>/v2.0/.well-known/openid-configuration'
  // or you can use the common endpoint
  // 'https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration'

  // Required
  clientID: process.env.AZURE_APP_CLIENT_ID,

  // Required.
  // If you are using the common endpoint, you should either set `validateIssuer` to false, or provide a value for `issuer`.
  validateIssuer: false,

  issuer: `https://login.microsoftonline.com/common/v2.0`,

  // Required.
  // Set to true if you use `function(req, token, done)` as the verify callback.
  // Set to false if you use `function(req, token)` as the verify callback.
  passReqToCallback: false,

  // Required if you are using common endpoint and setting `validateIssuer` to true.
  // For tenant-specific endpoint, this field is optional, we will use the issuer from the metadata by default.
  //issuer: "https://sts.windows.net/" + process.env.AZURE_APP_TENANT_GUID + "/",

  // Optional, default value is clientID
  //audience: 'api://033a44da-a38e-4679-a30a-3f0fdab7b0d9',

  // Optional. Default value is false.
  // Set to true if you accept access_token whose `aud` claim contains multiple values.
  allowMultiAudiencesInToken: true,

  // Optional. 'error', 'warn' or 'info'
  loggingLevel: "error",

  loggingNoPII: false,
};

var options = {
  // The URL of the metadata document for your app. We will put the keys for token validation from the URL found in the jwks_uri tag of the in the metadata.
  identityMetadata: creds.identityMetadata,
  clientID: creds.clientID,
  validateIssuer: creds.validateIssuer,
  issuer: creds.issuer,
  passReqToCallback: creds.passReqToCallback,
  isB2C: creds.isB2C,
  policyName: creds.policyName,
  allowMultiAudiencesInToken: creds.allowMultiAudiencesInToken,
  audience: creds.audience,
  loggingLevel: creds.loggingLevel,
};

// B2C

const B2Cconfig = {
  credentials: {
    tenantName: process.env.AZURE_APP_B2C_TENANT_NAME,
    clientID: process.env.AZURE_APP_B2C_CLIENT_ID,
  },
  policies: {
    policyName: "B2C_1_signupsignin1",
  },
  resource: {
    scope: ["access.user"],
  },
  metadata: {
    authority: "disastertechb2c.b2clogin.com",
    discovery: ".well-known/openid-configuration",
    version: "v2.0",
  },
  settings: {
    isB2C: true,
    validateIssuer: false,
    tenantIdOrName: process.env.AZURE_APP_TENANT_GUID,
    passReqToCallback: false,
    loggingLevel: "error",
  },
};

const B2Coptions = {
  identityMetadata: `https://${B2Cconfig.credentials.tenantName}.b2clogin.com/${B2Cconfig.credentials.tenantName}.onmicrosoft.com/${B2Cconfig.policies.policyName}/${B2Cconfig.metadata.version}/${B2Cconfig.metadata.discovery}`,
  clientID: B2Cconfig.credentials.clientID,
  audience: B2Cconfig.credentials.clientID,
  policyName: B2Cconfig.policies.policyName,
  isB2C: B2Cconfig.settings.isB2C,
  validateIssuer: B2Cconfig.settings.validateIssuer,
  tenantIdOrName: B2Cconfig.settings.tenantIdOrName,
  loggingLevel: B2Cconfig.settings.loggingLevel,
  passReqToCallback: B2Cconfig.settings.passReqToCallback,
};

// This is just an example of editgroup, but will expand to handle all standard auth measures so they don't have to be in the functions themselves
const authorization_validations = {
  "/dice/editgroup": [
    {
      fn: validateUserInGroups,
      argMapper: (req) => [req.request_user_guid, [req.body.group.group_guid]],
    },
    {
      fn: validateRBACPermissionForAction,
      argMapper: (req) => [
        req.request_user_guid,
        req.body.group.group_guid,
        "Edit Group Name",
      ],
    },
  ],
};

async function authorizations(endpoint_name, request) {
  if (!authorization_validations[endpoint_name]) {
    return 0;
  }

  const errors = await Promise.all(
    authorization_validations[endpoint_name].map(async (validator) => {
      const validationResult = await validator.fn(
        ...validator.argMapper(request)
      );
      return validationResult;
    })
  );

  return !!errors.filter((e) => !e).length;
}

export async function getUserGuidFromAuthUsername(auth_username) {
  const getUserGuidFromAuthUsernameSql =
    "SELECT user_guid from users WHERE email_address=$1;";
  const getUserGuidFromAuthUsernameResult = await dice_pool.query(
    getUserGuidFromAuthUsernameSql,
    [auth_username]
  );
  let user_guid = getUserGuidFromAuthUsernameResult.rows.length
    ? getUserGuidFromAuthUsernameResult.rows[0].user_guid
    : "";
  return user_guid;
}

export const auth = async (req, res, next) => {
  if (!req.headers.authorization) {
    logInformationSendResponse(
      "AUTH ERROR",
      req.url,
      '{"ERROR":"UNAUTHORIZED"}',
      "UNAUTHENTICATED USER",
      res,
      401
    );
    return;
  }

  // Return 401 if auth header improperly formatted
  if (!req.headers.authorization.substring(6)) {
    logInformationSendResponse(
      "AUTH ERROR",
      req.url,
      '{"ERROR":"UNAUTHORIZED"}',
      "UNAUTHENTICATED USER",
      res,
      401
    );
    return;
  }

  const authToken = jwt_decode(req.headers.authorization.substring(6));

  // Return 401 if authToken improperly formatted
  if (typeof authToken !== "object") {
    logInformationSendResponse(
      "AUTH ERROR",
      req.url,
      '{"ERROR":"UNAUTHORIZED"}',
      "UNAUTHENTICATED USER",
      res,
      401
    );
    return;
  }

  let bearerOptions = options;

  // AAD
  // authToken.iss.indexOf("login.microsoftonline.com") !== -1)
  // no change to default

  // B2C
  if (authToken.iss.indexOf("disastertechb2c.b2clogin.com") !== -1) {
    bearerOptions = B2Coptions;
  }

  const bearerStrategy = new BearerStrategy(bearerOptions, function (
    token,
    done
  ) {
    done(null, {}, token);
  });

  passport.use(bearerStrategy);

  // We want to get the request_user_guid at this step so we don't have to call it in EVERY function
  const request_user_guid = await getUserGuidFromAuthUsername(
    authToken.preferred_username || authToken.emails[0]
  );
  if (req.url !== "/createOrGetUser" && !request_user_guid.length) {
    logInformationSendResponse(
      "ERROR",
      req.url,
      '{"ERROR":"UNAUTHORIZED"}',
      request_user_guid,
      res,
      401
    );
    return;
  }
  req.request_user_guid = request_user_guid;

  const auth_errors = await authorizations(req.url, req);
  if (!!auth_errors) {
    logInformationSendResponse(
      "AUTH ERROR",
      req.url,
      '{"ERROR":"UNAUTHORIZED"}',
      request_user_guid,
      res,
      401
    );
    return;
  }

  try {
    passport.authenticate("oauth-bearer", { session: false })(req, res, next);
  } catch (e) {
    logInformationSendResponse(
      "ERROR",
      req.url,
      '{"ERROR":"BAD REQUEST"}',
      request_user_guid,
      res,
      400
    );
    return;
  }
};
