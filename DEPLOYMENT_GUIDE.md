🚀 Shark Bounty - Deployment Guide

📋 Prerequisites

Before deploying, ensure you have:
• ✅ Firebase account with Realtime Database
• ✅ Telegram Bot Token
• ✅ Vercel account (or similar hosting)
• ✅ Domain name (optional)


🔥 Firebase Setup

Step 1: Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add Project"
3. Enter project name: "Shark Bounty"
4. Disable Google Analytics (optional)
5. Click "Create Project"


Step 2: Enable Realtime Database
1. In Firebase Console, go to "Realtime Database"
2. Click "Create Database"
3. Choose location (closest to your users)
4. Start in **Test Mode** (we'll secure it later)
5. Click "Enable"


Step 3: Configure Database Rules

Replace the default rules with:


{
  "rules": {
    "users": {
      "$uid": {
        ".read": true,
        ".write": "$uid === auth.uid || !data.exists()"
      }
    },
    "tasks": {
      ".read": true,
      ".write": false
    },
    "redeemCodes": {
      ".read": true,
      ".write": false
    },
    "profileSections": {
      ".read": true,
      ".write": false
    }
  }
}


Step 4: Get Firebase Config
1. Go to Project Settings (gear icon)
2. Scroll to "Your apps"
3. Click "Web" icon (</>)
4. Register app name: "Shark Bounty Web"
5. Copy the config object


Step 5: Update index.html

Replace the Firebase config in `index.html` with your config:


const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT.firebaseio.com",
  projectId: "YOUR_PROJECT",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID",
  measurementId: "YOUR_MEASUREMENT_ID"
};


Step 6: Initialize Default Data

Run this in Firebase Console > Realtime Database:


{
  "redeemCodes": {
    "SHBK": { "amount": 5000 },
    "WELC": { "amount": 1000 },
    "GIFT": { "amount": 2500 },
    "STAR": { "amount": 10000 }
  },
  "tasks": {
    "task1": {
      "name": "Join Telegram Channel",
      "photo": "https://example.com/telegram-icon.png",
      "amount": 1000,
      "link": "https://t.me/your_channel"
    },
    "task2": {
      "name": "Follow Twitter",
      "photo": "https://example.com/twitter-icon.png",
      "amount": 500,
      "link": "https://twitter.com/your_account"
    },
    "task3": {
      "name": "Join Discord",
      "photo": "https://example.com/discord-icon.png",
      "amount": 750,
      "link": "https://discord.gg/your_server"
    }
  },
  "profileSections": {
    "roadmap": {
      "name": "RoadMap",
      "image": "https://github.com/akhterefti-del/Shark/blob/7e14b838bb95a2bb6ab2cc81008d2b69cfbe2d0b/readmap.png?raw=true",
      "link": "https://your-roadmap-link.com"
    },
    "presale": {
      "name": "Presale",
      "image": "https://github.com/akhterefti-del/Shark/blob/7e14b838bb95a2bb6ab2cc81008d2b69cfbe2d0b/presale.png?raw=true",
      "link": "https://your-presale-link.com"
    }
  }
}


🤖 Telegram Bot Setup

Step 1: Create Bot
1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose bot name: "Shark Bounty"
4. Choose username: "SharkBountybot" (or your choice)
5. Save the bot token


Step 2: Configure Bot

Send these commands to BotFather:


/setdescription
Tap to earn SHB tokens! Invite friends and complete tasks for rewards.

/setabouttext
Shark Bounty - The ultimate tap-to-earn game on Telegram!

/setuserpic
(Upload your bot profile picture)


Step 3: Set Web App URL
1. Deploy your site first (see Vercel section below)
2. Send `/newapp` to BotFather
3. Select your bot
4. Enter app title: "Shark Bounty"
5. Enter description
6. Upload app icon (512x512 PNG)
7. Enter Web App URL: `https://your-domain.vercel.app`
8. Choose inline mode: No


Step 4: Set Bot Commands

Send `/setcommands` to BotFather and paste:


start - Start earning SHB
help - Get help
balance - Check your balance
referral - Get referral link


🌐 Vercel Deployment

Method 1: GitHub Integration (Recommended)

Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com)
2. Click "New Repository"
3. Name: "shark-bounty"
4. Make it Public or Private
5. Click "Create Repository"


Step 2: Upload Files

# In your local folder with index.html
git init
git add index.html README.md FEATURES.md
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/shark-bounty.git
git push -u origin main


Step 3: Deploy to Vercel
1. Go to [Vercel](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure:
- Framework Preset: Other
- Root Directory: ./
- Build Command: (leave empty)
- Output Directory: (leave empty)
5. Click "Deploy"
6. Wait for deployment to complete
7. Copy your deployment URL


Method 2: Direct Upload

Step 1: Prepare Files
1. Create a folder named "shark-bounty"
2. Place `index.html` inside
3. Zip the folder


Step 2: Deploy
1. Go to [Vercel](https://vercel.com)
2. Click "Add New Project"
3. Click "Deploy" tab
4. Drag and drop your folder
5. Wait for deployment
6. Copy your deployment URL


🔗 Connect Bot to Web App

Step 1: Update Bot
1. Open BotFather
2. Send `/mybots`
3. Select your bot
4. Click "Bot Settings"
5. Click "Menu Button"
6. Click "Edit Menu Button URL"
7. Enter your Vercel URL: `https://your-app.vercel.app`


Step 2: Test Integration
1. Open your bot in Telegram
2. Click "Start" or the menu button
3. Web app should open
4. Test all features


🎯 Testing Referral System

Test Referral Links
1. Get your user ID from the profile section
2. Create test link: `https://t.me/SharkBountybot?start=r12345`
3. Open in different Telegram account
4. Verify 500 SHB is awarded to referrer
5. Check referral count increases


Test Redemption Codes
1. Go to Profile section
2. Enter code: `WELC`
3. Click Redeem
4. Verify SHB is added
5. Try same code again (should fail)


🔒 Security Hardening

Firebase Security Rules (Production)

{
  "rules": {
    "users": {
      "$uid": {
        ".read": true,
        ".write": "auth != null && auth.uid === $uid"
      }
    },
    "tasks": {
      ".read": true,
      ".write": "auth != null && root.child('admins').child(auth.uid).exists()"
    },
    "redeemCodes": {
      ".read": true,
      ".write": "auth != null && root.child('admins').child(auth.uid).exists()"
    },
    "profileSections": {
      ".read": true,
      ".write": "auth != null && root.child('admins').child(auth.uid).exists()"
    },
    "admins": {
      ".read": "auth != null && $uid === auth.uid",
      ".write": false
    }
  }
}


Add Admin Users

In Firebase Console, add admin UIDs:

{
  "admins": {
    "YOUR_USER_ID": true,
    "ANOTHER_ADMIN_ID": true
  }
}


📊 Monitoring & Analytics

Firebase Analytics
1. Enable Analytics in Firebase Console
2. View user engagement
3. Track events
4. Monitor performance


Custom Events (Optional)

Add to index.html:

// Track coin taps
firebase.analytics().logEvent('coin_tap', {
  amount: tapCount
});

// Track purchases
firebase.analytics().logEvent('purchase', {
  item: 'energy_booster',
  value: 10000
});


🐛 Troubleshooting

Issue: Referral not working

**Solution:**
1. Check URL format: `https://t.me/YourBot?start=r12345`
2. Verify Firebase rules allow writes
3. Check console for errors
4. Ensure referral ID is valid


Issue: Redemption codes not working

**Solution:**
1. Check code exists in Firebase
2. Verify code format (4 characters, uppercase)
3. Check Firebase rules
4. Ensure code hasn't been used


Issue: Coins not saving

**Solution:**
1. Check Firebase connection
2. Verify user ID is generated
3. Check browser console for errors
4. Ensure Firebase rules allow writes


Issue: Energy not recovering

**Solution:**
1. Check if timer is running
2. Verify energy < maxEnergy
3. Check for JavaScript errors
4. Refresh the page


🔄 Updates & Maintenance

Adding New Tasks
1. Go to Firebase Console
2. Navigate to Realtime Database
3. Under `tasks`, click "+"
4. Add new task object:

{
  "name": "Task Name",
  "photo": "https://image-url.com/icon.png",
  "amount": 1000,
  "link": "https://task-link.com"
}


Adding Redemption Codes
1. Go to Firebase Console
2. Navigate to `redeemCodes`
3. Add new code:

{
  "CODE": {
    "amount": 5000
  }
}


Updating Profile Sections
1. Go to Firebase Console
2. Navigate to `profileSections`
3. Edit existing or add new sections


📱 Custom Domain (Optional)

Vercel Custom Domain
1. Go to Vercel Dashboard
2. Select your project
3. Click "Settings" > "Domains"
4. Click "Add"
5. Enter your domain
6. Follow DNS configuration steps
7. Wait for verification


Update Bot URL
1. Update BotFather with new domain
2. Test all functionality
3. Update any hardcoded URLs


✅ Launch Checklist

Before going live:
• Firebase configured and secured
• All default data added
• Bot created and configured
• Web app deployed to Vercel
• Bot connected to web app
• Referral system tested
• Redemption codes tested
• All features working
• Mobile responsive checked
• Security rules applied
• Analytics enabled
• Custom domain configured (optional)
• Backup plan in place


🎉 Post-Launch

Marketing
1. Share referral links
2. Post on social media
3. Create promotional content
4. Engage with community


Monitoring
1. Check Firebase usage
2. Monitor user growth
3. Track engagement metrics
4. Respond to feedback


Maintenance
1. Add new tasks regularly
2. Create new redemption codes
3. Update features based on feedback
4. Fix bugs promptly


⸻


**Need Help?**
• Check Firebase Console for errors
• Review browser console logs
• Test in incognito mode
• Verify all URLs are correct


**Congratulations! Your Shark Bounty app is now live! 🎉**
