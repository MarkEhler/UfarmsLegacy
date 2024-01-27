import pg from "pg";
const { Pool } = pg;
import fs from "fs";

import dotenv from "dotenv";
import { updateNewUserMappingFormDICE } from "../routes/Groups/GroupsFnComponents.js";
if (process.env.RUN_FLAG?.trim() === "dev") {
  dotenv.config({ path: ".devEnv" });
} else {
  dotenv.config();
}

export const dice_pgcreds = {
  user: process.env.PGUSER?.trim(),
  host: process.env.PGHOST?.trim(),
  database: process.env.PGDICEDATABASE?.trim(),
  password: process.env.PGPASSWORD?.trim(),
  sslmode: "verify-full",
  ssl: {
    cert: fs.readFileSync("./root.crt").toString(),
  },
  port: 5432,
  max: 1000,
  idleTimeoutMillis: 100000,
  connectionTimeoutMillis: 100000,
};

export const epic_pgcreds = {
  user: process.env.PGUSER?.trim(),
  host: process.env.PGHOST?.trim(),
  database: process.env.PGEPICDATABASE?.trim(),
  password: process.env.PGPASSWORD?.trim(),
  sslmode: "verify-full",
  ssl: {
    cert: fs.readFileSync("./root.crt").toString(),
  },
  port: 5432,
  max: 1000,
  idleTimeoutMillis: 100000,
  connectionTimeoutMillis: 100000,
};

export const dice_pool = new Pool(dice_pgcreds);
export const epic_pool = new Pool(epic_pgcreds);
epic_pool.query("LISTEN epic_create_user");
epic_pool.on("notification", async (data) => {
  const payload = JSON.parse(data.payload);
  await updateNewUserMappingFormDICE(payload, dice_pool);
});

dice_pool.on("error", (err) => {
  console.error("An idle client has experienced an error", err.stack);
});
