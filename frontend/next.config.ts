import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "assets.aceternity.com",
        pathname: "/demos/**",
      },
      {
        protocol: "https",
        hostname: "picsum.photos",
        pathname: "/200/300",
      },
    ],
  },
};

export default nextConfig;
