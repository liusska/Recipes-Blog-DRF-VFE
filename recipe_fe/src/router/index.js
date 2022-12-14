import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import RecipesView from "@/views/RecipesView";
import CreateView from "@/views/CreateView";
import RecipeDetailsView from "@/views/RecipeDetailsView";
import RegisterView from "@/views/Auth/RegisterView";
import LoginView from "@/views/Auth/LoginView";
import ProfileView from "@/views/Auth/ProfileView";
import EditRecipeView from "@/views/EditRecipeView";
import DeleteRecipeView from "@/views/DeleteRecipeView";
import DessertsView from "@/views/DessertsView";
import LikedByUserView from "@/views/LikedByUserView";

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
        path: '/recipes/dessert',
        name: 'dessert',
        component: DessertsView
    },
    {
        path: '/recipes/:id',
        name: 'recipesDetails',
        component: RecipeDetailsView,
        props: true
    },
    {
        path: '/recipes/create',
        name: 'create',
        component: CreateView
    },
    {
        path: '/recipes/edit/:id',
        name: 'edit',
        component: EditRecipeView,
        props: true
    },
    {
        path: '/recipes/delete/:id',
        name: 'delete',
        component: DeleteRecipeView,
        props: true
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
        {
        path: '/profile/liked',
        name: 'liked',
        component: LikedByUserView
    },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
