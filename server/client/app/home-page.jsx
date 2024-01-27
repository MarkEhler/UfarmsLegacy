import RootLayout from "./layout";
import Link from "next/link";

export default function HomePage() {
  return (
    <RootLayout>
      <Link href="/">Home</Link>
    </RootLayout>
  );
}
