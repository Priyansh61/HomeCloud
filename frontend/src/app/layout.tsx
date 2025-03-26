import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "HomeCloud",
  description:
    "A self-hosted, privacy-focused alternative to Google Drive and Google Photos",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
