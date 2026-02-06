<!-- register.vue -->
<template>
  <view class="register-page">
    <!-- 顶部标题 -->
    <view class="header">
      <text class="title">AI取名</text>
      <text class="subtitle">开启宝宝取名之旅</text>
    </view>

    <!-- 注册表单 -->
    <view class="form-card card">
      <!-- 用户名 -->
      <view class="input-group">
        <text class="label">用户名</text>
        <view class="input-wrap">
          <input
            v-model="form.username"
            class="input"
            type="text"
            placeholder="2-12位字母/数字/中文"
            placeholder-class="placeholder"
            maxlength="12"
          />
        </view>
      </view>

      <!-- 邮箱 -->
      <view class="input-group">
        <text class="label">邮箱</text>
        <view class="input-wrap">
          <input
            v-model="form.email"
            class="input"
            type="text"
            placeholder="用于接收验证码"
            placeholder-class="placeholder"
            maxlength="50"
          />
        </view>
      </view>

      <!-- 验证码 -->
      <view class="input-group">
        <text class="label">验证码</text>
        <view class="code-wrap">
          <input
            v-model="form.code"
            class="input code-input"
            type="number"
            placeholder="请输入6位验证码"
            placeholder-class="placeholder"
            maxlength="6"
          />
          <button
            class="code-btn"
            :class="{ disabled: countdown > 0 }"
            @click="onSendCode"
            :disabled="countdown > 0"
          >
            {{ countdown > 0 ? `${countdown}s 后重发` : '获取验证码' }}
          </button>
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
            placeholder="6-20位，建议含字母+数字"
            placeholder-class="placeholder"
            maxlength="20"
          />
        </view>
      </view>

      <!-- 确认密码 -->
      <view class="input-group">
        <text class="label">确认密码</text>
        <view class="input-wrap">
          <input
            v-model="form.confirmPassword"
            class="input"
            type="password"
            placeholder="请再次输入密码"
            placeholder-class="placeholder"
            maxlength="20"
          />
        </view>
      </view>

      <!-- 注册按钮 -->
      <button class="btn register-btn" @click="onRegister" :disabled="loading">
        {{ loading ? '注册中...' : '立即注册' }}
      </button>

      <!-- 登录引导 -->
      <view class="login-prompt">
        <text class="prompt-text">已有账号？</text>
        <text class="login-link" @click="onGotoLogin">立即登录</text>
      </view>
    </view>
  </view>
</template>

<script setup>
import { ref, reactive } from 'vue'

const form = reactive({
  username: '',
  email: '',
  code: '',
  password: '',
  confirmPassword: ''
})

const loading = ref(false)
const countdown = ref(0) // 倒计时

// 发送验证码
const onSendCode = () => {
  if (!form.email.trim()) {
    uni.showToast({ title: '请输入邮箱', icon: 'none' })
    return
  }
  const emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailReg.test(form.email)) {
    uni.showToast({ title: '邮箱格式不正确', icon: 'none' })
    return
  }

  // 模拟发送
  uni.showToast({ title: '验证码已发送', icon: 'success' })
  countdown.value = 60
  const timer = setInterval(() => {
    if (countdown.value > 0) {
      countdown.value--
    } else {
      clearInterval(timer)
    }
  }, 1000)
}

const onRegister = () => {
  if (!form.username.trim()) {
    uni.showToast({ title: '请输入用户名', icon: 'none' })
    return
  }
  if (form.username.length < 2) {
    uni.showToast({ title: '用户名至少2位', icon: 'none' })
    return
  }
  if (!form.email.trim()) {
    uni.showToast({ title: '请输入邮箱', icon: 'none' })
    return
  }
  const emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailReg.test(form.email)) {
    uni.showToast({ title: '邮箱格式不正确', icon: 'none' })
    return
  }
  if (!form.code.trim()) {
    uni.showToast({ title: '请输入验证码', icon: 'none' })
    return
  }
  if (form.code.length !== 6) {
    uni.showToast({ title: '验证码为6位数字', icon: 'none' })
    return
  }
  if (!form.password.trim()) {
    uni.showToast({ title: '请输入密码', icon: 'none' })
    return
  }
  if (form.password.length < 6) {
    uni.showToast({ title: '密码至少6位', icon: 'none' })
    return
  }
  if (form.password !== form.confirmPassword) {
    uni.showToast({ title: '两次密码不一致', icon: 'none' })
    return
  }

  loading.value = true
  uni.showLoading({ title: '注册中...' })

  // 模拟请求
  setTimeout(() => {
    loading.value = false
    uni.hideLoading()
    uni.showToast({ title: '注册成功！', icon: 'success' })
    uni.redirectTo({ url: '/pages/login/login' }) // 注册成功跳登录
  }, 1000)
}

const onGotoLogin = () => {
  uni.redirectTo({ url: '/pages/login/login' })
}
</script>

<style scoped>
page {
  background: linear-gradient(135deg, #fef9f0 0%, #ffebe6 100%);
  padding: 20rpx;
}

.register-page {
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

.input-wrap,
.code-wrap {
  position: relative;
  width: 100%;
  min-height: 88rpx;
  display: flex;
}

.input {
  flex: 1;
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

.code-input {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
  border-right: none;
}

.code-btn {
  width: 180rpx;
  height: 88rpx;
  font-size: 26rpx;
  background: #f8f8f8;
  color: #e74c3c;
  border: 2rpx solid #e0e0e0;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-left: none;
}

.code-btn:not(.disabled):hover,
.code-btn:not(.disabled):active {
  background: #fff2f0;
  border-color: #ff9e80;
  color: #e74c3c;
}

.code-btn.disabled {
  opacity: 0.6;
  color: #aaa;
}

.register-btn {
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

.register-btn:active {
  transform: scale(0.96);
}

.register-btn[disabled] {
  opacity: 0.6;
}

.login-prompt {
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

.login-link {
  color: #e74c3c;
  font-weight: 500;
}
</style>