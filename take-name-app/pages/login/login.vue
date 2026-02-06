<!-- login.vue -->
<template>
  <view class="login-page">
    <!-- 顶部标题 -->
    <view class="header">
      <text class="title">AI取名</text>
      <text class="subtitle">请登录您的账号</text>
    </view>

    <!-- 登录表单 -->
    <view class="form-card card">
      <!-- 邮箱 -->
      <view class="input-group">
        <text class="label">邮箱</text>
        <view class="input-wrap">
          <input
            v-model="form.email"
            class="input"
            type="text"
            placeholder="请输入注册邮箱"
            placeholder-class="placeholder"
            maxlength="50"
          />
        </view>
      </view>

      <!-- 密码 -->
      <view class="input-group">
        <text class="label">密码</text>
        <view class="input-wrap">
          <input
            v-model="form.password"
            class="input"
            type="password"
            placeholder="请输入密码"
            placeholder-class="placeholder"
            maxlength="20"
          />
        </view>
      </view>

      <!-- 登录按钮 -->
      <button class="btn login-btn" @click="onLogin" :disabled="loading">
        {{ loading ? '登录中...' : '立即登录' }}
      </button>

      <!-- 注册引导 -->
      <view class="signup-prompt">
        <text class="prompt-text">还没有账号？</text>
        <text class="signup-link" @click="onGotoRegister">立即注册</text>
      </view>
    </view>
  </view>
</template>

<script setup>
import { ref, reactive } from 'vue'
import http from "/http/http.js"

const form = reactive({
  email: '',
  password: ''
})

const loading = ref(false)

const onLogin = async () => {
  if (!form.email.trim()) {
    uni.showToast({ title: '请输入邮箱', icon: 'none' })
    return
  }
  if (!form.password.trim()) {
    uni.showToast({ title: '请输入密码', icon: 'none' })
    return
  }

  // 正则校验邮箱（简单版）
  const emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailReg.test(form.email)) {
    uni.showToast({ title: '邮箱格式不正确', icon: 'none' })
    return
  }

  loading.value = true
  uni.showLoading({ title: '登录中...' })
  
  // 发起网络请求
  try{
	  let result = await http.login(form.email, form.password);
	  uni.showToast({ title: '登录成功', icon: 'success' });
	  console.log(result);
	  let user = result.user;
	  let token = result.token;
	  uni.setStorageSync("user", user);
	  uni.setStorageSync("token", token);
	  // 跳转到首页
	  uni.redirectTo({
	  	url: "/pages/index/index"
	  })
  }catch(e){
	  uni.showToast({
	  	title: e.message,
		icon: none
	  })
  }finally{
	  loading.value = false;
	  uni.hideLoading();
  }
}

const onGotoRegister = () => {
  uni.navigateTo({ url: '/pages/register/register' })
}
</script>

<style scoped>
page {
  background: linear-gradient(135deg, #fef9f0 0%, #ffebe6 100%);
  padding: 20rpx;
}

.login-page {
  min-height: 100vh;
  padding: 0 24rpx;
}

.header {
  text-align: center;
  margin-bottom: 40rpx;
}

.title {
  font-size: 48rpx;
  font-weight: 700;
  color: #e74c3c;
  display: block;
  margin-bottom: 12rpx;
}

.subtitle {
  font-size: 28rpx;
  color: #888;
}

.card {
  background: #ffffff;
  border-radius: 24rpx;
  box-shadow: 0 8rpx 30rpx rgba(231, 76, 60, 0.12);
  padding: 40rpx 32rpx;
  margin-bottom: 32rpx;
}

.input-group {
  margin-bottom: 36rpx;
}

.label {
  display: block;
  font-size: 30rpx;
  color: #555;
  margin-bottom: 16rpx;
  font-weight: 500;
}

.input-wrap {
  position: relative;
  width: 100%;
  min-height: 88rpx;
}

.input {
  width: 100%;
  height: 88rpx;
  padding: 24rpx 28rpx;
  border-radius: 16rpx;
  background: #fafafa;
  border: 2rpx solid #e0e0e0;
  font-size: 30rpx;
  color: #333;
  box-sizing: border-box;
  cursor: text;
  user-select: text;
  -webkit-tap-highlight-color: transparent;
}

.input:focus {
  border-color: #ff9e80;
  background: #fff9f8;
  transform: scale(1.005);
}

.placeholder {
  color: #aaa;
}

.forgot-password {
  text-align: right;
  margin-bottom: 36rpx;
}

.forgot-text {
  font-size: 26rpx;
  color: #e74c3c;
}

.login-btn {
  height: 88rpx;
  line-height: 88rpx;
  font-size: 32rpx;
  font-weight: 600;
  border-radius: 50rpx;
  color: #fff;
  background: linear-gradient(135deg, #ff9e80, #e74c3c);
  border: none;
  box-shadow: 0 6rpx 20rpx rgba(0, 0, 0, 0.1);
}

.login-btn:active {
  transform: scale(0.96);
}

.login-btn[disabled] {
  opacity: 0.6;
}

.signup-prompt {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 32rpx;
  font-size: 28rpx;
  color: #888;
}

.prompt-text {
  margin-right: 8rpx;
}

.signup-link {
  color: #e74c3c;
  font-weight: 500;
}
</style>