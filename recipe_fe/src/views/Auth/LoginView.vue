<template>
    <NavBar/>

    <form @submit.prevent="LoginFunc">
        <label>Email</label>
        <input type="email" required v-model="email">

        <label>Password</label>
        <input type="password" required v-model="password">


         <div class="error" v-if="errors.length">
             <ul v-for="error in errors" :key="error">
                 <li>{{ error }}</li>
             </ul>
         </div>

        <div class="submit">
            <button class="login-button">Login</button>
        </div>
        * Or <router-link to="/register">click here</router-link> to register

    </form>
    <div class="footer">
        <Footer />
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";

export default {
    components: {NavBar, Footer},
    data() {
        return {
            email: '',
            password: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'Login | Recipes Blog'
    },
    methods: {
        async LoginFunc() {
            document.title = 'Login | Recipes Blog'
            const formData = {
                email: this.email,
                password: this.password,
            }

            await axios
                .post('/auth/login/', formData)
                .then( response => {
                    if(response.status === 200) {
                        localStorage.setItem('token', response.data.token)
                        localStorage.getItem('token')
                        axios.defaults.headers.common['Authorization'] = localStorage.getItem('token')
                        this.$router.push('/')
                    }
                })
                .catch(error => {
                        if (error.response){
                            for (const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            console.log(JSON.stringify(error))
                        }
                    })
        },
    }
}
</script>

<style scoped>
    form {
        max-width: 420px;
        margin: 30px auto;
        background: white;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label {
        color: #aaa;
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input, select {
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    input[type="checkbox"] {
        display: inline-block;
        width: 16px;
        margin: 0 10px 0 0;
        position: relative;
        top: 2px
    }
    .login-button{
        background: #0b6dff;
        border: 0;
        padding: 10px 20px;
        margin-top: 20px;
        color: white;
        border-radius: 20px;
    }
    .login-button:hover{
        cursor: pointer;
    }
    .submit {
        text-align: center;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
    }
</style>