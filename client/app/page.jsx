"use client";

import { useState } from "react";
import loginStyles from "./login-button.module.css";
import Link from "next/link";
import RootLayout from "./layout";
import ModalTemplate from "./components/modal-template";
import LoginForm from "./components/login-form";
import UserInfoForm from "./components/user-info-form";

export default function Home() {
  const [loginShown, setLoginShown] = useState(true);
  const [userFormShown, setUserFormShown] = useState(false);

  return (
    <RootLayout>
      <Link href="/map">See the Map</Link>
      <button className={loginStyles.login} onClick={() => setLoginShown(true)}>
        Login
      </button>
      <button onClick={() => setUserFormShown(true)}>Show User Form</button>

      <ModalTemplate
        isOpen={loginShown}
        closeModal={() => setLoginShown(false)}
      >
        <LoginForm />
      </ModalTemplate>

      <ModalTemplate
        isOpen={userFormShown}
        closeModal={() => setUserFormShown(false)}
      >
        <UserInfoForm />
      </ModalTemplate>
    </RootLayout>
  );
}
