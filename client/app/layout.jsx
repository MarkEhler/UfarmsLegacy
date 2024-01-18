import "../styles/global.css";
import styles from "./map.module.css";

export const metadata = {
  title: "Home",
  description: "Welcome to Ufarms",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header className={styles.header}>
          <h1 className={styles.logo}>[Ufarms logo]</h1>
          <button className={styles.login}>Log In</button>
        </header>

        {children}
      </body>
    </html>
  );
}
