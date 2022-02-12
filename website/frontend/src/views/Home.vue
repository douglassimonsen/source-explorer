<template>
  <div class="home">
    <graph-dependencies/>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import GraphDependencies from "@/components/GraphDependencies.vue"; // @ is an alias to /src

@Options({
  components: {
    GraphDependencies,
  },
})
export default class Home extends Vue {}
</script>
