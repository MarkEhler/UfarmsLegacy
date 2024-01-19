import RootLayout from "../layout";
import Link from "next/link";

export const metadata = {
  title: "Ufarms - Map",
};

export default function Map() {
  return (
    <RootLayout>
      <Link href="/">Home</Link>
    </RootLayout>
  );
}
