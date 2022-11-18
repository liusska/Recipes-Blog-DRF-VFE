import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import RecipesView from "@/views/RecipesView";
import CreateView from "@/views/CreateView";
import RecipeDetailsView from "@/views/RecipeDetailsView";
import RegisterView from "@/views/Auth/RegisterView";
import LoginView from "@/views/Auth/LoginView";
import ProfileView from "@/views/Auth/ProfileView";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/recipes',
        name: 'recipes',
        component: RecipesView
    },
    {
        path: '/recipes/:id',
        name: 'recipesDetails',
        component: RecipeDetailsView,
        props: true
    },
    {
        path: '/create',
        name: 'create',
        component: CreateView
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterView
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },

    {
        path: '/profile',
        name: 'profile',
        component: ProfileView
    },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
