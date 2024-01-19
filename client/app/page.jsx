"use client";

import { useState } from "react";
import loginStyles from "./login-button.module.css";
import Link from "next/link";
import RootLayout from "./layout";
import ModalTemplate from "./components/modal-template";
import LoginForm from "./components/login-form";

export default function Home() {
  const [modalShown, setModalShown] = useState(false);

  return (
    <RootLayout>
      <Link href="/map">See the Map</Link>
      <button className={loginStyles.login} onClick={() => setModalShown(true)}>
        Login
      </button>

      <ModalTemplate
        isOpen={modalShown}
        closeModal={() => setModalShown(false)}
      >
        <LoginForm />
      </ModalTemplate>
    </RootLayout>
  );
}
