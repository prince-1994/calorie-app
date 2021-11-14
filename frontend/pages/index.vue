<template>
  <div>
    <section class="section">
      <div class="buttons">
        <b-button
          type="is-danger"
          outlined
          icon-right="plus"
          tag="nuxt-link"
          to="/edit/"
          >Add New Entry</b-button
        >
      </div>
      <hr />
      <form @submit.prevent="fetchEntries">
        <div class="is-flex is-justify-content-space-between">
          <div class="columns">
            <div class="column">
              <b-field label="Start Date">
                <b-datepicker
                  v-model="startDate"
                  placeholder="Select a start date..."
                  icon="calendar-today"
                >
                </b-datepicker>
              </b-field>
            </div>
            <div class="column">
              <b-field label="End Date">
                <b-datepicker
                  v-model="endDate"
                  placeholder="Select a end date..."
                  icon="calendar-today"
                >
                </b-datepicker>
              </b-field>
            </div>
          </div>
          <div class="is-flex buttons is-align-content-center">
            <b-button
              native-type="submit"
              tag="router-link"
              :to="`/?consumed_at__gte=${startDate}&consumed_at__lt=${endDate}`"
              type="is-primary"
              >Submit</b-button
            >
          </div>
        </div>
      </form>
      <day-food-entry-card
        v-for="dateData in allDatesData"
        :key="dateData.dateStr"
        :date-str="dateData.dateStr"
        :entries="dateData.entries"
        :total-calorie="dateData.totalCalorie"
        :has-reached-limit="dateData.hasReachedLimit"
      >
      </day-food-entry-card>
    </section>
    <section class=""></section>
  </div>
</template>

<script>
import DayFoodEntryCard from '../components/DayFoodEntryCard.vue'
export default {
  name: 'HomePage',
  components: { DayFoodEntryCard },
  middleware: ['auth'],

  async asyncData({ query, $repositories, store }) {
    const response = await $repositories.foodEntries.index({ params: query })
    const data = {}
    const dateOptions = { year: 'numeric', month: 'numeric', day: 'numeric' }
    const timeOptions = {
      hour: 'numeric',
      minute: 'numeric',
      second: 'numeric',
    }
    for (const item of response) {
      const dateTime = new Date(item.consumedAt)
      const timeStr = dateTime.toLocaleDateString('en-US', timeOptions)
      const dateStr = dateTime.toLocaleDateString('en-US', dateOptions)
      item.dateStr = dateStr
      item.timeStr = timeStr
      if (!data[dateStr]) {
        data[dateStr] = {
          dateStr,
          date: new Date(dateStr),
          entries: [],
          totalCalorie: 0,
          hasReachedLimit: false,
        }
      }
      data[dateStr].entries.push(item)
      if (!item.isInactive) {
        data[dateStr].totalCalorie += item.calorie
        data[dateStr].hasReachedLimit =
          data[dateStr].totalCalorie >= store.state.userProfile.calorieLimit
      }
    }

    const allDatesData = Object.values(data)
    allDatesData.sort((a, b) => b.date - a.date)
    return {
      allDatesData,
    }
  },

  data() {
    return {
      startDate: null,
      endDate: null,
    }
  },

  computed: {
    submitQueryLink() {
      return ''
    },
  },
  watchQuery: [
    'consumed_at__gte',
    'consumed_at__lt',
    'consumed_at__lte',
    'consumed_at__gt',
  ],
}
</script>
