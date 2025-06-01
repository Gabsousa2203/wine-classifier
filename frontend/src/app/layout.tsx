import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "react-hot-toast";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Wine Quality Classifier",
  description: "Clasificador de calidad de vinos usando IA",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body className={inter.className}>
        <Toaster position="top-center" />
        <main className="min-h-screen bg-gradient-to-br from-purple-900 via-red-800 to-amber-900">
          {children}
        </main>
      </body>
    </html>
  );
}
