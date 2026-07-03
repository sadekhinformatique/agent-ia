import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { prompt } = await req.json();
  // TODO: prompt → image (Gemini, Ideogram, etc.)
  return NextResponse.json({ status: "generated", url: "stub_image_url" });
}
