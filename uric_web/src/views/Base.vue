<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible>
      <div class="logo"
           style="font-style: italic;text-align: center;font-size: 30px;color:#fff;margin: 10px 0;line-height: 50px;font-family: 'Times New Roman'">
        <span>DevOps</span>
      </div>
      <div class="logo"/>
      <a-menu v-for="menu in menu_list" v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-menu-item v-if="menu.children.length===0" :key="menu.id">

          <router-link :to="menu.menu_url">
            <desktop-outlined/>
            <span> {{ menu.title }}</span>
          </router-link>
        </a-menu-item>

        <a-sub-menu v-else :key="menu.id">
          <template #title>
            <span>
              <user-outlined/>
              <span>{{ menu.title }}</span>
            </span>
          </template>
          <a-menu-item v-for="child_menu in menu.children" :key="child_menu.id">
            <router-link :to="child_menu.menu_url">{{ child_menu.title }}</router-link>
          </a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 20px">
        <a-row type="flex" justify="start">
          <a-col :span="6">
            <a-breadcrumb  :routes="menu_list">
<!--              <a-breadcrumb-item href="/">-->
<!--                <home-outlined/>-->
<!--              </a-breadcrumb-item>-->
                <template #itemRender="{ route, paths }">
               <span v-if="menu_list.indexOf(route) === menu_list.length - 1">
                {{ route.breadcrumbName }}
               </span>
                  <router-link v-else :to="`${basePath}/${paths.join('/')}`">
                    {{ route.breadcrumbName }}
                  </router-link>
                </template>
            </a-breadcrumb>
          </a-col>

          <a-col :span="1" :offset="17">
            <a-breadcrumb>
              <a-breadcrumb-item>
                <a-button @click="logout" type="primary" class="logout">
                  ??????
                </a-button>
              </a-breadcrumb-item>

            </a-breadcrumb>
          </a-col>

        </a-row>

      </a-layout-header>

      <a-layout-content style="margin: 0 16px">

        <router-view></router-view>

      </a-layout-content>
      <a-layout-footer style="text-align: center">
        Design ??2023 Created by CG
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script>


import {
  DesktopOutlined,
  FileOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
  HomeOutlined
} from '@ant-design/icons-vue';
import {defineComponent, ref} from 'vue';


export default defineComponent({
  setup() {
    const checked = ref(true);

    return {
      checked,
    };
  },
  components: {
    PieChartOutlined,
    DesktopOutlined,
    UserOutlined,
    TeamOutlined,
    FileOutlined,
    HomeOutlined,
  },
  created() {
    // console.log(this.$route.matched.length)
    // console.log($router)

  },
  data() {
    return {
      basePath: "/uric",
      collapsed: ref(false),
      selectedKeys: ref(['1']),
      menu_list: [
        {
          id: 1, icon: 'mail', title: '????????????', tube: '', 'menu_url': '/uric/show_center', children: []
        },
        {
          id: 2, icon: 'mail', title: '????????????', 'menu_url': '/uric/host', children: []
        },
        {
          id: 3, icon: 'bold', title: '????????????', tube: '', menu_url: '/uric/workbench',
          children: [
            {id: 10, icon: 'mail', title: '????????????', 'menu_url': '/uric/multi_exec'},
            {id: 11, icon: 'mail', title: '????????????', 'menu_url': '/uric/multi_exec'},
          ]
        },
        // {
        //   id: 4, icon: 'highlight', title: '????????????', tube: '', menu_url: '/uric/workbench', children: [
        //     {id: 12, title: '????????????', menu_url: '/uric/release'},
        //     {id: 13, title: '????????????', menu_url: '/uric/release'}
        //   ]
        // },
        // {id: 5, icon: 'mail', title: '????????????', tube: '', menu_url: '/uric/workbench', children: []},
        // {
        //   id: 6, icon: 'mail', title: '????????????', tube: '', menu_url: '/uric/workbench', children: [
        //     {id: 14, title: '????????????', 'menu_url': '/uric/environment'},
        //     {id: 15, title: '????????????', 'menu_url': '/uric/workbench'},
        //     {id: 16, title: '????????????', 'menu_url': '/uric/workbench'}
        //   ]
        // },
        // {id: 7, icon: 'mail', title: '????????????', tube: '', 'menu_url': '/uric/workbench', children: []},
        // {
        //   id: 8, icon: 'mail', title: '??????', tube: '', 'menu_url': '/uric/workbench', children: [
        //     {id: 17, title: '????????????', 'menu_url': '/uric/workbench'},
        //     {id: 18, title: '???????????????', 'menu_url': '/uric/workbench'},
        //     {id: 19, title: '???????????????', 'menu_url': '/uric/workbench'}
        //   ]
        // },
        // {
        //   id: 9, icon: 'mail', title: '????????????', tube: '', menu_url: '/uric/workbench', children: [
        //     {id: 20, title: '????????????', tube: '', menu_url: '/uric/workbench'},
        //     {id: 21, title: '????????????', tube: '', menu_url: '/uric/workbench'},
        //     {id: 22, title: '????????????', tube: '', menu_url: '/uric/workbench'}
        //   ]
        // }
      ]
    };
  },
  methods: {
    logout() {
      let self = this;
      this.$confirm({
        title: 'Uric????????????',
        content: '??????????????????????????????',
        onOk() {
          self.$store.commit('setToken', '')
          self.$router.push('/login')
        }
      })
    },
  }

});
</script>
<style>
#components-layout-demo-side .logo {
  height: 32px;
  margin: 16px;
}

.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}

.logout {
  line-height: 1.5715;
}
</style>