<script setup lang="ts">
import { withBase } from "vitepress";

defineProps<{
  src: string;
  alt?: string;
  width?: string | number;
}>();
</script>

<template>
  <div class="doc-figure">
    <img :src="withBase(src)" :alt="alt ?? ''" :style="{ width: `${width ?? 80}%` }" loading="lazy" />
  </div>
</template>
