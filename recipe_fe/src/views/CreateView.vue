<template>
    <form  @submit.prevent="createPost">
        <label>Title</label>
        <input type="text" v-model="title">

        <label>Ingredients</label>
        <input type="text" v-model="ingredients">

        <label>Category:</label>
        <select v-model="category">
            <option v-for="option in options" :value="option.value">
                {{ option.text }}
            </option>
        </select>

        <label>Photo</label>
        <input type="url" v-model="photo">

        <label>Video</label>
        <input type="url" v-model="video">

        <label>Time</label>
        <input type="text" v-model="time_in_minutes">

        <label>Description</label>
        <textarea cols="76" rows="10" v-model="description"></textarea>

        <div class="submit">
            <button>Create post</button>
        </div>
    </form>

    <div v-if=" error ">
        <strong>{{ error }}</strong>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'CreateView',
    data() {
        return {
            title: '',
            ingredients: '',
            category: '',
            photo: '',
            video: '',
            time_in_minutes: '',
            description: '',

            error: '',
            options: [
                {text: 'Others', value: 'Others'},
                {text: 'Dessert', value: 'Dessert'},
                {text: 'Snack', value: 'Snack'},
                {text: 'Salad', value: 'Salad'},
                {text: 'Baked', value: 'Baked'},
                {text: 'Main', value: 'Main'},
                {text: 'Pizza', value: 'Pizza'},
            ]
        }
    },
    methods: {
        createPost(){
            const dataForm = {
                title: this.title,
                ingredients: this.ingredients,
                category: this.category,
                photo: this.photo,
                video: this.photo,
                time_in_minutes: this.time_in_minutes,
                description: this.description,
            }
            axios.post('/recipes/', dataForm)
            .then(resp =>{
                console.log(resp)
            })
            .then(data => {
                console.log(data)
            })
            .catch(error => {
                this.error = error
                console.log(error)
            })
            window.location.reload()
            this.$router.push('/recipes')
        }
    }
}
</script>

<style scoped>
    form {
        max-width: 600px;
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
        font-size: 0.8em;
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
    textarea{
        border-color: snow;
    }

    button {
        background: #0b6dff;
        border: 0;
        padding: 10px 20px;
        margin-top: 20px;
        color: white;
        border-radius: 20px;
    }
    .submit {
        text-align: center;
    }
</style>