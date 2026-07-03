import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { text } = await req.json();
  // TODO: texte → carrousel PNG
  return NextResponse.json({ status: "generated", slides: 8 });
}
