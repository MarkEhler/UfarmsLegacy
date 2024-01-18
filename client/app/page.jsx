import HomePage from "./home-page";

import Link from "next/link";
import RootLayout from "./layout";
import utilStyles from "../styles/utils.module.css";

export default function Home() {
  return (
    <RootLayout home>
      <Link href="/map">See the Map</Link>

      <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
        <h2 className={utilStyles.headingLg}>Blog</h2>

        <ul className={utilStyles.list}>
          <li>Oh Hey</li>
        </ul>
      </section>

      <header>
        <h1>[Ufarms logo]</h1>
        <button>Log In</button>
      </header>

      <Link href="/">Home</Link>
    </RootLayout>
  );
}
