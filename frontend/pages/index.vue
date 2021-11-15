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
              :to="dateQueryLink"
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
  </div>
</template>

<script>
import DayFoodEntryCard from '../components/DayFoodEntryCard.vue'
export default {
  name: 'HomePage',
  components: { DayFoodEntryCard },
  middleware: ['auth'],

  async asyncData({ query, $repositories, store }) {
    const startDateStr = query.startDate
      ? new Date(query.startDate).toISOString()
      : null
    const day = 60 * 60 * 24 * 1000
    const tempEndDate = query.endDate
      ? new Date(new Date(query.endDate).getTime() + day)
      : null
    const endDateStr = tempEndDate ? tempEndDate.toISOString() : null
    if (
      startDateStr &&
      endDateStr &&
      new Date(startDateStr) > new Date(endDateStr)
    ) {
      store.dispatch('addMessage', {
        message: 'Start date should be less than end Date.',
        type: 'error',
      })
    }
    const response = await $repositories.foodEntries.index({
      params: {
        consumed_at__gte: startDateStr,
        consumed_at__lt: endDateStr,
      },
    })
    const data = {}
    const dateOptions = { year: 'numeric', month: 'long', day: 'numeric' }
    const timeOptions = { hour: '2-digit', minute: '2-digit' }
    for (const item of response) {
      const dateTime = new Date(item.consumedAt)
      const timeStr = dateTime.toLocaleTimeString('en-US', timeOptions)
      const dateStr = dateTime.toLocaleDateString('en-US', dateOptions)
      item.dateStr = dateStr
      item.timeStr = timeStr
      item.consumedAtDate = dateTime
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
    for (const item of allDatesData) {
      item.entries.sort((a, b) => a.consumedAtDate - b.consumedAtDate)
    }
    return {
      allDatesData,
      startDate: query.startDate ? new Date(query.startDate) : null,
      endDate: query.endDate ? new Date(query.endDate) : null,
    }
  },

  computed: {
    dateQueryLink() {
      const startDateStr = this.startDate ? this.startDate.toISOString() : null
      const endDateStr = this.endDate ? this.endDate.toISOString() : null
      if (startDateStr && endDateStr) {
        return `/?startDate=${startDateStr}&endDate=${endDateStr}`
      } else if (startDateStr) {
        return `/?startDate=${startDateStr}`
      } else if (endDateStr) {
        return `/?endDate=${endDateStr}`
      } else {
        return '/'
      }
    },
  },
  watchQuery: ['startDate', 'endDate'],
}
</script>
