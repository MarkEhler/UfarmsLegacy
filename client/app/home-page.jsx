"use client";

import Link from "next/link";

export default function HomePage() {
  return (
    <>
      <header>
        <h1>[Ufarms logo]</h1>
        <button>Log In</button>
      </header>

      <Link href="/">Home</Link>
    </>
  );
}
