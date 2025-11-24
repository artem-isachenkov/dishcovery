// "use server";

// import { create } from "zustand";
// import { persist } from "zustand/middleware";

type User = {
  id: string;
  app_metadata: {
    provider: string;
    providers: string[];
  };
  user_metadata: {
    email: string;
    email_verified: boolean;
    phone_verified: boolean;
    sub: string;
  };
  aud: string;
  confirmation_sent_at: string | null;
  recovery_sent_at: string | null;
  email_change_sent_at: string | null;
  new_email: string | null;
  new_phone: string | null;
  invited_at: string | null;
  action_link: string | null;
  email: string;
  phone: string;
  created_at: string;
  confirmed_at: string | null;
  email_confirmed_at: string;
  phone_confirmed_at: string | null;
  last_sign_in_at: string;
  role: string;
  updated_at: string;
  identities: {
    id: string;
    identity_id: string;
    user_id: string;
    identity_data: {
      email: string;
      email_verified: boolean;
      phone_verified: boolean;
      sub: string;
    };
    provider: string;
    created_at: string;
    last_sign_in_at: string;
    updated_at: string;
  }[];
  is_anonymous: boolean;
  factors: unknown[];
};

export type Session = {
  provider_token: string | null;
  provider_refresh_token: string | null;
  access_token: string; // "eyJhbGciOiJIUzI1NiIsImtpZCI6ImpvWUh2N3hTMDNNVzVqZEoiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3ZkdmxreXdvcXhoYXBweXphcHpuLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJmNzlhYjk0Zi0wM2E4LTQ0ZGMtYWE0Ny05ZWM1Njk1ODgwZTciLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzM2ODczNDQ3LCJpYXQiOjE3MzY4Njk4NDcsImVtYWlsIjoiZGV2N0B0ZXN0LmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJkZXY3QHRlc3QuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiZjc5YWI5NGYtMDNhOC00NGRjLWFhNDctOWVjNTY5NTg4MGU3In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3MzY4Njk4NDd9XSwic2Vzc2lvbl9pZCI6IjU5M2Y1ZDZjLTIxY2MtNGI5Zi04MDUwLWZmYTg1ZTIwNzYzOSIsImlzX2Fub255bW91cyI6ZmFsc2V9.OKYmviLB71lVivDBxc0EmZmAE4obRmsZXNGs8mdoeMY";
  refresh_token: string; // "uP1aX7udJWZ7exBUujjYaQ";
  expires_in: number;
  expires_at: number;
  token_type: string; // "bearer";
  user: User;
};

// export type Auth = {
//   user: User;
//   session: Session;
// };

// export const useAuthStore = create(
//   persist<{ user: Session | null; setUser: (user: Session | null) => void }>(
//     (set) => ({
//       user: null as Session | null,
//       setUser: (user: Session | null) => set({ user }),
//       //   bears: 0,
//       //   increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
//       //   removeAllBears: () => set({ bears: 0 }),
//       //   updateBears: (newBears) => set({ bears: newBears }),
//     }),
//     {
//       name: "auth-storage",
//     }
//   )
// );
