"use server";

import { client } from "./client";
import qs from "qs";
import { Session } from "./store";
import { removeUserSession, setUserSession } from "./session";
import { Category, Many, Recipe } from "./models";

export const signup = async (email: string, password: string) => {
  const response = await client.post<Session>("/auth/sign-up/", {
    email,
    password,
  });
  if (response.status === 200) await setUserSession(response.data);
  return response.data;
};

export const signin = async (email: string, password: string) => {
  const response = await client.post<Session>(
    "/auth/sign-in/",
    qs.stringify({ username: email, password }),
    { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
  );

  if (response.status === 200) await setUserSession(response.data);
  return response.data;
};

export const me = async () => {
  const response = await client.get("/auth/me/");
  return response.data;
};

export const signout = async () => {
  const response = await client.post<{ id: string }>("/auth/sign-out/");
  await removeUserSession();
  return response.data;
};

export const fetchRecipes = async () => {
  const response = await client.get<Many<Recipe>>("/recipes/");
  return response.data;
};

export const fetchRecipe = async (id: number) => {
  const response = await client.get<Recipe>(`/recipes/${id}`);
  return response.data;
};

export const fetchCategories = async () => {
  const response = await client.get<Many<Category>>("/categories/");
  return response.data;
};

export const fetchCategory = async (id: number) => {
  const response = await client.get<Category>(`/categories/${id}`);
  return response.data;
};
