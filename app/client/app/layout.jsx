import "../styles/global.css";
import hdr from "./header.module.css";

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>Ufarms</title>
      </head>
      <body>
        <header className={hdr.header}>
          <h1 className={hdr.logo}>[Ufarms logo]</h1>
        </header>

        {children}
      </body>
    </html>
  );
}
