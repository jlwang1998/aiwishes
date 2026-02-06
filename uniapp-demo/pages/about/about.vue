<template>
	<view>
		<h1>我是about页面</h1>
		<view>用户名：{{ username }}</view>
		<view>
			<input type="text" placeholder="手机号" v-model="mobile">
		</view>
		<button @click="onLogin">登录</button>
		<br>
		<view>
			<view v-if="weather == '晴'">今天出去玩</view>
			<view v-else-if="weather == '阴'">今天去图书馆</view>
			<view v-else>今天待在家里</view>
		</view>
		
		<table>
			<tbody>
				<tr v-for="(book, index) in books" :key="book.name">
					<td>{{index+1}}</td>
					<td>{{book.name}}</td>
					<td>{{book.author}}</td>
				</tr>
			</tbody>
		</table>
	</view>
</template>

<script setup>
	import {ref, watch} from "vue";
	
	// 为什么要定义成ref类型呢？
	// 为了script中username的值发生改变，template中也会自动更新
	let username = ref("null");
	// 模拟网络请求
	setTimeout(() => {
		username.value = "张三";
	}, 2000);
	
	
	// 定义获取手机号的变量
	let mobile = ref("");
	watch(mobile, (value, oldValue) => {
		console.log("mobile: "+mobile.value);
	})
	
	
	const onLogin = () => {
		console.log("点击了登录");
	}
	
	
	let weather = ref("雨");
	
	let books = ref([{
		"name": "三国演义",
		"author": "罗贯中"
	}, {
		"name": "水浒传",
		"author": "施耐庵"
	}, {
		"name": "红楼梦",
		"author": "曹雪芹"
	}, {
		"name": "西游记",
		"author": "吴承恩"
	}])
	
</script>

<style>
	       
</style>
