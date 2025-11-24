export type Many<T> = {
  data: T[];
  count: number | null;
};

export type Category = {
  id: number;
  name: string;
  created_at: string;
  updated_at: string;
  description: string | null;
};

export type Recipe = {
  id: number;
  user_id: string;
  created_at: string;
  updated_at: string;
  title: string;
  description: string | null;
  category_id: number | null;
  category: Category | null;
};
