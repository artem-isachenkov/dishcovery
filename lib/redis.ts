"use server";

import { createClient } from "redis";

const client = createClient({
  username: process.env.REDIS_USER,
  password: process.env.REDIS_PASSWORD,
  socket: {
    host: process.env.REDIS_HOST,
    port: parseInt(process.env.REDIS_PORT || "6379"),
  },
});

client.on("error", (err) => {
  console.error("Redis error: ", err);
});

await client.connect();

export default async function getRedisClient() {
  return client;
}
