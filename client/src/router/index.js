import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/views/Home.vue'
import Course from '@/views/Course.vue'
import CourseView from '@/views/CourseView.vue'
import Contact from '@/views/Contact.vue'
import Faq from '@/views/Faq.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/corsi',
    name: 'course_list',
    component: Course
  },
  {
    path: '/corsi/:id',
    name: 'course',
    component: CourseView
  },
  {
    path: '/contatti',
    name: 'contact',
    component: Contact
  },
  {
    path: '/faq',
    name: 'faq',
    component: Faq
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
