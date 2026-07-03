import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { markdown } = await req.json();
  // TODO: appeler Puppeteer pour convertir markdown → PDF
  return NextResponse.json({ status: "generated", format: "pdf", slides: 10 });
}
