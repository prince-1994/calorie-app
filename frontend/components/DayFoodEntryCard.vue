<template>
  <div class="">
    <hr />
    <div class="is-flex is-justify-content-space-between">
      <div>
        <p>
          <span class="is-size-5">{{ dateStr }}</span>
          <b-tag v-show="hasReachedLimit" type="is-danger"
            >Limit Exceeded</b-tag
          >
        </p>
      </div>
      <div>
        <p>{{ totalCalorie }} Calories</p>
      </div>
    </div>

    <div
      v-for="entry in entries"
      :key="entry.id"
      class="is-flex is-justify-content-space-between box"
    >
      <div class="">
        <div class="is-flex is-justify-content-space-between">
          <p>{{ entry.timeStr }}</p>
          <b-tag v-show="entry.isInactive" type="is-info">Cheat</b-tag>
        </div>
        <p>{{ entry.calorie }}</p>
      </div>
      <b-button
        type="is-danger"
        size="is-small"
        outlined
        icon-right="pencil"
        tag="nuxt-link"
        :to="`/edit/${entry.id}`"
        >Manage</b-button
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'DayFoodEntryCard',
  props: {
    entries: {
      type: Array,
      default: () => [],
    },

    dateStr: {
      type: String,
      default: null,
    },

    totalCalorie: {
      type: Number,
      default: 0,
    },

    hasReachedLimit: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style></style>
