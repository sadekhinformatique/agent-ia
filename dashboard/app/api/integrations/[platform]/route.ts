import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest, { params }: { params: { platform: string } }) {
  const { action } = await req.json();
  // TODO: synchro vers Gmail, YouTube, Drive, Fireflies
  return NextResponse.json({ platform: params.platform, action, status: "synced" });
}
