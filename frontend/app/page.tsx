"use client";
import Image from "next/image";

import ConversationalAi from "./features/conversational-ai";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
          <ConversationalAi/>
      </div>
    </main>
  );
}
