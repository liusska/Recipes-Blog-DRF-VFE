<template>
        <nav>
            <div>
                <ul>
                    <li><router-link class="home-button" to="/"><i class="fa fa-home"></i>Home</router-link></li>
                    <li><router-link to="/recipes">Recipes</router-link></li>
                    <li><router-link to="/recipes/create" v-if="is_logged">Create</router-link></li>
                </ul>
            </div>
            <div class="profile-box">
                <router-link class="profile" to="/profile" v-if="is_logged"><i class="fa fa-user">&nbsp;&nbsp;Profile</i></router-link>
                <button class="button control" @click="logout()" v-if="is_logged">Logout</button>
                <ul>
                    <li><router-link to="/register" v-if="!is_logged">Register</router-link></li>
                    <li><router-link to="/login" v-if="!is_logged">Login</router-link></li>
                </ul>
            </div>

    </nav>
</template>

<script>
import axios from "axios";

export default {
    data(){
        return{
            is_logged: (localStorage.getItem('token') !== null),
        }
    },
    mounted() {

    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            this.$router.push('/login')
        },
    },
}
</script>

<style scoped>

nav {
    width: 100%;
    margin-right: 0;
    padding: 18px 2px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #2f2f2f;
}
nav ul li {
    list-style: none;
    display: inline-block;
    margin: 0 20px;
    position: relative;
}
nav ul li a{
    text-decoration: none;
    color: #fff;
    font-size: 20px;
    text-transform: uppercase;
}

nav ul li::after {
    content: '';
    height: 3px;
    width: 0;
    background: #009688;
    position: absolute;
    left: 0;
    bottom: -10px;
    transition: 0.5s;
}

nav ul li:hover::after{
    width: 100%;
}

.profile-box{
    display: flex;
    justify-content: flex-end;
    width: 30%;
    margin-right: 0;
}
.profile {
    color: white;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 20px;
    margin-right: 50px;
    padding: 4px;
}
i{
    padding-right: 10px;
}


</style>