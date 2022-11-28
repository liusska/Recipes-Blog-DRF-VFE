<template>
    <NavBar/>
    <form @submit.prevent="editPost" enctype="multipart/form-data">
        <label>Title</label>
        <input type="text" v-model="recipe_before.title">

        <label>Ingredients</label>
        <input type="text" v-model="recipe_before.ingredients">

        <label>Category:</label>
        <select v-model="recipe_before.category">
            <option v-for="option in options" :value="option.value">
                {{ option.text }}
            </option>
        </select>

        <label>Photo</label>
        <input type="file" ref="file" @change="selectFile" accept="image/*"/>

        <label>Video</label>
        <input type="url" v-model="recipe_before.video">

        <label>Time</label>
        <input type="text" v-model="recipe_before.time_in_minutes">

        <label>Description</label>
        <textarea cols="76" rows="10" v-model="recipe_before.description"></textarea>

        <div class="submit">
            <button>Edit post</button>
        </div>
    </form>

    <div v-if="error">
        <strong>{{ error }}</strong>
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    name: 'EditRecipeView',
    components: {NavBar},
    props: ['id'],
    data() {
        return {
            recipe_before: {},
            image_before: null,
            options: [
                {text: 'Others', value: 'Others'},
                {text: 'Dessert', value: 'Dessert'},
                {text: 'Snack', value: 'Snack'},
                {text: 'Salad', value: 'Salad'},
                {text: 'Baked', value: 'Baked'},
                {text: 'Main', value: 'Main'},
                {text: 'Pizza', value: 'Pizza'},
            ],
            error: '',
        }
    },
    mounted() {
        console.log("recipe id: " + this.id)
        axios.get(`/recipes/${this.id}`)
            .then(data => {
                this.image_before = data.data.photo
                this.recipe_before = data.data
            })
            .catch(err => console.log(err.messages))
    },
    methods: {
        editPost() {
            console.log('Image old ' + this.image_before)
            console.log('Obj photo ' + this.recipe_before.photo)
            // if (this.recipe_before.photo === null){
            //     this.recipe_before.photo = this.image_before
            // }
            this.recipe_before.photo = null

            console.log('New obj ', this.recipe_before)

            axios.put(`/recipes/${this.id}/`, this.recipe_before, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => console.log(resp))
                .catch(error => {
                    this.error = error
                    console.log(error)
                })
            this.$router.push(`/recipes/${this.recipe_before.id}`)
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