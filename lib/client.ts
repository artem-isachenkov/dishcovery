"use server";

import axios from "axios";
import { getUserSession } from "./session";

export const client = axios.create({
  baseURL: "http://backend:8000",
});

client.interceptors.request.use(
  async (config) => {
    "use server";
    const session = await getUserSession();
    console.log("🚀 ~ session:", session)

    if (session)
      config.headers.Authorization = `Bearer ${session.access_token}`;
    console.log("🚀 ~ config:", config);
    return config;
  },
  (error) => Promise.reject(error)
);

// client.interceptors.response.use(
//   (response) => {
//     // if (response.request.path.includes("auth/sign-out"))
//     //   delete client.defaults.headers.common.Authorization;

//     // if (
//     //   response.status === 200 &&
//     //   response.request.path.includes("auth/sign-in")
//     // ) {
//     //   // console.log("response.data:", response.data);
//     //   const token = response.data.access_token;

//     //   if (token)
//     //     client.defaults.headers.common.Authorization = `Bearer ${token}`;
//     // }

//     return response;
//   },
//   (error) => Promise.reject(error)
// );
