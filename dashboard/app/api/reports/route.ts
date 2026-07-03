import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { analytics } = await req.json();
  // TODO: analytics → rapport PDF visuel
  return NextResponse.json({ status: "generated", format: "pdf" });
}
