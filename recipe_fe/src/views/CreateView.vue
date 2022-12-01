<template>
    <NavBar/>
    <form @submit.prevent="createPost" enctype="multipart/form-data">
        <label>Title</label>
        <input type="text" v-model="title">

        <label>Ingredients</label>
        <input type="text" v-model="ingredients" placeholder="enter ingredients here separate by comma...">

        <label>Category:</label>
        <select v-model="category">
            <option v-for="option in options" :value="option.value">
                {{ option.text }}
            </option>
        </select>

        <label>Photo</label>
        <input type="file" ref="file" @change="selectFile" accept="image/*"/>

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
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    name: 'CreateView',
    components: {NavBar},
    data() {
        return {
            title: '',
            ingredients: '',
            category: '',
            photo: null,
            photo_obj: null,
            video: null,
            time_in_minutes: '',
            description: '',

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
    mounted() {

    },
    methods: {
        async createPost() {
            console.log(this.photo)
            const dataForm = {
                title: this.title,
                ingredients: this.ingredients,
                category: this.category,
                photo: this.photo,
                photo_obj: this.photo,
                video: this.video,
                time_in_minutes: this.time_in_minutes,
                description: this.description,
            }
            await axios.post('/recipes/', dataForm, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => console.log(resp))
                .catch(error => console.log(error))

            this.$router.push(`/recipes`)
        },

        selectFile() {
            this.photo = this.$refs.file.files.item(0)
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

::placeholder {
    color: #555555;
    font-style: italic;
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

textarea {
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