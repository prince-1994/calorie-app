<template>
  <div>
    <div class="box">
      <form @submit.prevent="">
        <b-field label="Name">
          <b-input v-model="updateFoodEntry.name"></b-input>
        </b-field>
        <b-field label="Calorie">
          <b-input v-model="updateFoodEntry.calorie"></b-input>
        </b-field>
        <b-field label="Consumption Date/Time">
          <b-datetimepicker
            v-model="updateFoodEntry.consumedAt"
            placeholder="Click to select..."
          ></b-datetimepicker>
        </b-field>

        <b-field>
          <b-switch v-model="updateFoodEntry.isInactive"
            ><span class="has-text-weight-bold">Cheat</span></b-switch
          >
        </b-field>
        <div class="buttons">
          <b-button type="is-primary" @click="saveEntry">Save</b-button>
          <b-button v-if="foodEntry.id" type="is-danger" @click="deleteEntry"
            >Delete</b-button
          >
          <b-button type="is-danger" outlined @click="cancel">Cancel</b-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ $repositories, params, query }) {
    let foodEntry = {}

    if (params.id) {
      foodEntry = await $repositories.foodEntries.show(params.id)
    }
    return {
      foodEntry,
      updateFoodEntry: {
        name: foodEntry.name || '',
        calorie: foodEntry.calorie || 0,
        isInactive: foodEntry.isInactive || false,
        consumedAt: foodEntry.consumedAt
          ? new Date(foodEntry.consumedAt)
          : new Date(),
      },
      source: query.source,
    }
  },

  methods: {
    saveEntry() {
      let result = null
      this.$nuxt.$loading.start()
      if (this.foodEntry.id) {
        result = this.$repositories.foodEntries.update(
          this.foodEntry.id,
          this.updateFoodEntry
        )
      } else {
        result = this.$repositories.foodEntries.create(this.updateFoodEntry)
      }

      result
        .then((result) => {
          this.foodEntry = result
          this.$router.go(-1)
        })
        .catch((err) => {
          this.$store.dispatch('addTemporaryMessage', {
            message: err.response,
            type: 'error',
          })
        })
        .finally(() => {
          this.$nuxt.$loading.finish()
        })
    },

    deleteEntry() {
      this.$nuxt.$loading.start()
      this.$repositories.foodEntries
        .delete(this.foodEntry.id)
        .then(() => {
          this.$router.go(-1)
        })
        .finally(() => {
          this.$nuxt.$loading.finish()
        })
    },

    cancel() {
      this.$router.go(-1)
    },
  },
}
</script>

<style></style>
