"use server";

import { cookies } from "next/headers";
import { Session } from "./store";
import getRedisClient from "./redis";

export const setUserSession = async (data: Session) => {
  const redis = await getRedisClient();
  await redis.hSet("sessions", data.user.id, JSON.stringify(data));
  const cookieStore = await cookies();
  cookieStore.set("session", data.user.id, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    expires: new Date(data.expires_at),
    sameSite: "lax"
  });
  // const sessionData = cookieStore.get("session");
  // console.log("🚀 ~ setUserSession ~ sessionData:", sessionData?.value);
};

export const removeUserSession = async () => {
  const cookieStore = await cookies();
  const id = cookieStore.get("session");

  if (!id) return;

  const redis = await getRedisClient();
  await redis.hDel("sessions", id.value);
  cookieStore.delete("session");
};

export const getUserSession = async (): Promise<Session | null> => {
  const cookieStore = await cookies();
  const id = cookieStore.get("session");
  console.log("🚀 ~ getUserSession ~ id:", id);
  if (!id) return null;
  const redis = await getRedisClient();
  const data = await redis.hGet("sessions", id.value);
  if (!data) return null;
  console.log("🚀 ~ getUserSession ~ data:", data);
  return JSON.parse(data);
};
