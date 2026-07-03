import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest, { params }: { params: Promise<{ platform: string }> }) {
  const { platform } = await params;
  const { action } = await req.json();
  return NextResponse.json({ platform, action, status: "synced" });
}
