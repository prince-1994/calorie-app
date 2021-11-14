<template>
  <div class="box">
    <div class="is-flex is-justify-content-space-between">
      <div>
        <p>
          <span class="is-size-5"
            ><strong>{{ dateStr }}</strong></span
          >
          <b-tag v-show="hasReachedLimit" class="mr-2" type="is-danger"
            >Limit Exceeded</b-tag
          >
        </p>
      </div>
      <div>
        <p>
          <strong>{{ totalCalorie }} Calories</strong>
        </p>
      </div>
    </div>
    <hr />
    <b-table :data="entries">
      <b-table-column field="name" label="Item Name" width="">
        <template #default="props">
          {{ props.row.name }}
        </template>
      </b-table-column>

      <b-table-column field="timeStr" label="Time">
        <template #default="props">
          {{ props.row.timeStr }}
        </template>
      </b-table-column>
      <b-table-column field="calorie" label="Calories">
        <template #default="props">
          {{ props.row.calorie }}
        </template>
      </b-table-column>
      <b-table-column field="cheat" label="Info">
        <template #default="props">
          <b-tag v-show="props.row.isInactive" type="is-info">Cheat</b-tag>
        </template>
      </b-table-column>
      <b-table-column field="manage" label="Manage">
        <template #default="props">
          <b-button
            type="is-success"
            icon-left="pencil"
            tag="router-link"
            :to="`/edit/${props.row.id}`"
          ></b-button>
        </template>
      </b-table-column>
    </b-table>

    <!-- <div
      v-for="(entry, index) in entries"
      :key="entry.id"
      class="is-flex is-justify-content-space-between box"
    >
      <div class="">
        <div class="is-flex is-justify-content-space-between">
          <div>{{ index + 1 }}.</div>
          <div class="mx-2">{{ entry.name }} - {{ entry.timeStr }}</div>

          <div class="mx-2">{{ entry.calorie }} calories</div>
          <b-tag v-show="entry.isInactive" type="is-info">Cheat</b-tag>
        </div>
      </div>
      <b-button
        type="is-danger"
        outlined
        icon-right="pencil"
        tag="nuxt-link"
        :to="`/edit/${entry.id}`"
        >Manage</b-button
      >
    </div> -->
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
