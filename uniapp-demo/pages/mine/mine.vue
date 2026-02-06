<template>
	<view>
		<h1>我的页面</h1>
		<view>姓名：{{person.name}}</view>
		<view>年龄：{{person.age}}</view>
		<button @click="onClick">点击我</button>
	</view>
</template>

<script setup>
	import {reactive, onMounted} from "vue";
	
	let person = reactive({
		"name": "张三",
		"age": 18
	})
	
	const onClick = () => {
		person.name = "李四"
	}
	
	onMounted(() => {
		// 一般会请求服务器的数据，获取到了以后给变量赋值
		console.log("onMounted生命周期方法！");
	})
</script>

<style>
	       
</style>
