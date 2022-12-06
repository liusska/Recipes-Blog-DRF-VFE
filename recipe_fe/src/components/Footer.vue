<template>
    <footer>
    <p>
        Copyright &copy;2022 | Designed by <span>Lyudmila Sokolova &nbsp;</span>
        <a href="https://www.linkedin.com/in/liusska/" target="_blank">
            <i class="fa fa-linkedin"></i>
        </a>
    </p>
</footer>

</template>

<script>
export default {
    name: "Footer"
}
</script>

<style scoped>
footer{
    background: #555555;
    font-size: 16px;
    color: white;
    padding: 5px 20px;

}

footer p {
    margin: 2px;
}

.fa.fa-linkedin {
    color: white;
}
</style>