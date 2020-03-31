from edtools import *
from bs4 import BeautifulSoup
from html5print import CSSBeautifier
import jsbeautifier



code = '''

<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en" id="home"><head>

    
    <meta charset="utf-8" />
    <meta name="google-site-verification" content="f0LCrdI6z4Fo8zld4sHCgo5SiUE4EYYRUa6KVeX3Mw8" />
    <meta name="msvalidate.01" content="4C77784AFD61498FA0764E14D1631D53" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
    
    <title>Stripe - Online payment processing for internet businesses</title>

<style type="text/css" media="screen">#ui-datepicker-div.booked_custom_date_picker table.ui-datepicker-calendar tbody td a.ui-state-active,#ui-datepicker-div.booked_custom_date_picker table.ui-datepicker-calendar tbody td a.ui-state-active:hover,body #booked-profile-page input[type=submit].button-primary:hover,body .booked-list-view button.button:hover, body .booked-list-view input[type=submit].button-primary:hover,body table.booked-calendar input[type=submit].button-primary:hover,body .booked-modal input[type=submit].button-primary:hover,body table.booked-calendar th,body table.booked-calendar thead,body table.booked-calendar thead th,body table.booked-calendar .booked-appt-list .timeslot .timeslot-people button:hover,body #booked-profile-page .booked-profile-header,body #booked-profile-page .booked-tabs li.active a,body #booked-profile-page .booked-tabs li.active a:hover,body #booked-profile-page .appt-block .google-cal-button > a:hover,#ui-datepicker-div.booked_custom_date_picker .ui-datepicker-header{ background:#0073AA !important; }body #booked-profile-page input[type=submit].button-primary:hover,body table.booked-calendar input[type=submit].button-primary:hover,body .booked-list-view button.button:hover, body .booked-list-view input[type=submit].button-primary:hover,body .booked-modal input[type=submit].button-primary:hover,body table.booked-calendar th,body table.booked-calendar .booked-appt-list .timeslot .timeslot-people button:hover,body #booked-profile-page .booked-profile-header,body #booked-profile-page .appt-block .google-cal-button > a:hover{ border-color:#0073AA !important; }body table.booked-calendar tr.days,body table.booked-calendar tr.days th,body .booked-calendarSwitcher.calendar,body #booked-profile-page .booked-tabs,#ui-datepicker-div.booked_custom_date_picker table.ui-datepicker-calendar thead,#ui-datepicker-div.booked_custom_date_picker table.ui-datepicker-calendar thead th{ background:#015e8c !important; }body table.booked-calendar tr.days th,body #booked-profile-page .booked-tabs{ border-color:#015e8c !important; }#ui-datepicker-div.booked_custom_date_picker table.ui-datepicker-calendar tbody td.ui-datepicker-today a,#ui-datepicker-div.booked_custom_date_picker table.ui-datepicker-calendar tbody td.ui-datepicker-today a:hover,body #booked-profile-page input[type=submit].button-primary,body table.booked-calendar input[type=submit].button-primary,body .booked-list-view button.button, body .booked-list-view input[type=submit].button-primary,body .booked-list-view button.button, body .booked-list-view input[type=submit].button-primary,body .booked-modal input[type=submit].button-primary,body table.booked-calendar .booked-appt-list .timeslot .timeslot-people button,body #booked-profile-page .booked-profile-appt-list .appt-block.approved .status-block,body #booked-profile-page .appt-block .google-cal-button > a,body .booked-modal p.booked-title-bar,body table.booked-calendar td:hover .date span,body .booked-list-view a.booked_list_date_picker_trigger.booked-dp-active,body .booked-list-view a.booked_list_date_picker_trigger.booked-dp-active:hover,.booked-ms-modal .booked-book-appt /* Multi-Slot Booking */{ background:#56C477; }body #booked-profile-page input[type=submit].button-primary,body table.booked-calendar input[type=submit].button-primary,body .booked-list-view button.button, body .booked-list-view input[type=submit].button-primary,body .booked-list-view button.button, body .booked-list-view input[type=submit].button-primary,body .booked-modal input[type=submit].button-primary,body #booked-profile-page .appt-block .google-cal-button > a,body table.booked-calendar .booked-appt-list .timeslot .timeslot-people button,body .booked-list-view a.booked_list_date_picker_trigger.booked-dp-active,body .booked-list-view a.booked_list_date_picker_trigger.booked-dp-active:hover{ border-color:#56C477; }body .booked-modal .bm-window p i.fa,body .booked-modal .bm-window a,body .booked-appt-list .booked-public-appointment-title,body .booked-modal .bm-window p.appointment-title,.booked-ms-modal.visible:hover .booked-book-appt{ color:#56C477; }.booked-appt-list .timeslot.has-title .booked-public-appointment-title { color:inherit; }</style>

    <meta name="description" content="Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes, including fraud prevention, and subscription management. Use Stripe’s payment platform to accept and process payments online for easy-to-use commerce solutions." />


    <link rel="shortcut icon" href="/favicon.ico" />

    <link rel="apple-touch-icon-precomposed" href="/img/apple-touch-icon/180x180.png" />
    <link rel="icon" href="/img/apple-touch-icon/180x180.png" />


    <link rel="image_src" type="image/png" href="https://stripe.com/img/v3/home/social.png" />

    

  <link rel="alternate" href="https://stripe.com/" hreflang="en-us" />
  <link rel="alternate" href="https://stripe.com/au" hreflang="en-au" />
  <link rel="alternate" href="https://stripe.com/ca" hreflang="en-ca" />
  <link rel="alternate" href="https://stripe.com/gb" hreflang="en-gb" />
  <link rel="alternate" href="https://stripe.com/ie" hreflang="en-ie" />
  <link rel="alternate" href="https://stripe.com/nz" hreflang="en-nz" />

        <link rel="alternate" href="https://stripe.com/?locale=de" hreflang="de" />
    <link rel="alternate" href="https://stripe.com/" hreflang="en" />
    <link rel="alternate" href="https://stripe.com/?locale=es" hreflang="es" />
    <link rel="alternate" href="https://stripe.com/?locale=fr" hreflang="fr" />
    <link rel="alternate" href="https://stripe.com/?locale=it" hreflang="it" />
    <link rel="alternate" href="https://stripe.com/?locale=ja" hreflang="ja" />


        <link rel="canonical" href="https://stripe.com/" />

    <meta property="og:title" content="Stripe - Online payment processing for internet businesses" />
    <meta property="og:url" content="https://stripe.com/" />
    <meta property="og:description" content="Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes, including fraud prevention, and subscription management. Use Stripe’s payment platform to accept and process payments online for easy-to-use commerce solutions." />
    <meta property="og:image" content="https://stripe.com/img/v3/home/social.png" />

      <meta name="twitter:card" content="summary" />
      <meta name="twitter:image" content="https://stripe.com/img/v3/home/twitter.png" />
    <meta name="twitter:site" content="@stripe" />
    <meta name="twitter:title" content="Stripe - Online payment processing for internet businesses" />
    <meta name="twitter:description" content="Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes, including fraud prevention, and subscription management. Use Stripe’s payment platform to accept and process payments online for easy-to-use commerce solutions." />


    <script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js" nonce=""></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-W8NSNKQ"></script><script src="https://connect.facebook.net/signals/config/742650679237989?v=2.8.37&amp;r=stable" async=""></script><script async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script type="application/json" id="strut_files">{&amp;quot;v3/shared/navigation_ie10.css&amp;quot;:&amp;quot;/assets/compiled/js/../css/sprockets-css-v3/shared/navigation_ie10-8f2f65ac24a2d0c7f862.min.css&amp;quot;,&amp;quot;v3/home/animations.js&amp;quot;:&amp;quot;/assets/compiled/js/sprockets-js-v3/home/animations-8f2f65ac24a2d0c7f862.min.js&amp;quot;,&amp;quot;v3/shared/prism_light.css&amp;quot;:&amp;quot;/assets/compiled/js/../css/sprockets-css-v3/shared/prism_light-8f2f65ac24a2d0c7f862.min.css&amp;quot;}</script>

    <script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Corporation",
    "name": "Stripe",
    "url": "https://stripe.com/",
    "logo": "https://stripe.com/img/about/logos/logos/blue.png",
    "contactPoint" : [
      {
        "@type" : "ContactPoint",
        "url": "https://stripe.com/contact",
        "email": "info@stripe.com",
        "contactType": "customer support"
      }
    ],
    "sameAs": [
      "https://www.facebook.com/StripeHQ/",
      "https://twitter.com/stripe",
      "https://www.linkedin.com/company/stripe"
    ]
  }
</script>

    <script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Country",
    "address": {
      "addressCountry": "US"
    }
  }
</script>

      <link rel="preload" href="/fonts/stripe-icons.woff2" as="font" type="font/woff2" crossorigin="" />
  <link rel="preload" href="/fonts/camphor-ss/300-light.woff2" as="font" type="font/woff2" crossorigin="" />
  <link rel="preload" href="/fonts/camphor-ss/400-regular.woff2" as="font" type="font/woff2" crossorigin="" />
  <link rel="preload" href="/fonts/camphor-ss/500-medium.woff2" as="font" type="font/woff2" crossorigin="" />
  <link rel="preload" href="/fonts/camphor-ss/600-bold.woff2" as="font" type="font/woff2" crossorigin="" />


<script nonce="">        !function(){if('PerformanceLongTaskTiming' in window){var g=window.__tti={e:[]};
        g.o=new PerformanceObserver(function(l){g.e=g.e.concat(l.getEntries())});
        g.o.observe({entryTypes:['longtask']})}}();
</script>
      <link rel="stylesheet" href="/assets/compiled/js/../css/sprockets-css-v3/default-8f2f65ac24a2d0c7f862.min.css" />
  <link rel="stylesheet" href="/assets/compiled/js/../css/sprockets-css-v3/home/index-8f2f65ac24a2d0c7f862.min.css" />

  <script defer="" src="/assets/compiled/js/sprockets-js-v3/default-8f2f65ac24a2d0c7f862.min.js"></script>
  <script defer="" src="https://embed.runkit.com"></script>
  <script defer="" src="/assets/compiled/js/sprockets-js-v3/home/index-8f2f65ac24a2d0c7f862.min.js"></script>



    

  <link href="/assets/compiled/js/../css/sprockets-css-v3/shared/prism_light-8f2f65ac24a2d0c7f862.min.css" rel="stylesheet" /><script src="/assets/compiled/js/sprockets-js-v3/home/animations-8f2f65ac24a2d0c7f862.min.js"></script></head>

  <body>

    

    <header class="globalNav noDropdownTransition initialized">


  <div class="container-lg">
    <nav>
      <ul class="navRoot">


        <li class="navSection logo">
          <a class="rootLink item-home colorize" href="/" aria-label="Stripe homepage"><h1><svg xmlns="http://www.w3.org/2000/svg" width="62" height="25"><title>Stripe</title><path d="M5 10.1c0-.6.6-.9 1.4-.9 1.2 0 2.8.4 4 1.1V6.5c-1.3-.5-2.7-.8-4-.8C3.2 5.7 1 7.4 1 10.3c0 4.4 6 3.6 6 5.6 0 .7-.6 1-1.5 1-1.3 0-3-.6-4.3-1.3v3.8c1.5.6 2.9.9 4.3.9 3.3 0 5.5-1.6 5.5-4.5.1-4.8-6-3.9-6-5.7zM29.9 20h4V6h-4v14zM16.3 2.7l-3.9.8v12.6c0 2.4 1.8 4.1 4.1 4.1 1.3 0 2.3-.2 2.8-.5v-3.2c-.5.2-3 .9-3-1.4V9.4h3V6h-3V2.7zm8.4 4.5L24.6 6H21v14h4v-9.5c1-1.2 2.7-1 3.2-.8V6c-.5-.2-2.5-.5-3.5 1.2zm5.2-2.3l4-.8V.8l-4 .8v3.3zM61.1 13c0-4.1-2-7.3-5.8-7.3s-6.1 3.2-6.1 7.3c0 4.8 2.7 7.2 6.6 7.2 1.9 0 3.3-.4 4.4-1.1V16c-1.1.6-2.3.9-3.9.9s-2.9-.6-3.1-2.5H61c.1-.2.1-1 .1-1.4zm-7.9-1.5c0-1.8 1.1-2.5 2.1-2.5s2 .7 2 2.5h-4.1zM42.7 5.7c-1.6 0-2.5.7-3.1 1.3l-.1-1h-3.6v18.5l4-.7v-4.5c.6.4 1.4 1 2.8 1 2.9 0 5.5-2.3 5.5-7.4-.1-4.6-2.7-7.2-5.5-7.2zm-1 11c-.9 0-1.5-.3-1.9-.8V10c.4-.5 1-.8 1.9-.8 1.5 0 2.5 1.6 2.5 3.7 0 2.2-1 3.8-2.5 3.8z"/></svg></h1></a>
        </li>

        <li class="navSection primary">
          <button class="rootLink item-products hasDropdown colorize" data-dropdown="products" aria-haspopup="true" aria-expanded="false">
            <span>Products</span>
          </button>
          <button class="rootLink item-developers hasDropdown colorize" data-dropdown="developers" aria-haspopup="true" aria-expanded="false">
            <span>Developers</span>
          </button>
          <button class="rootLink item-company hasDropdown colorize" data-dropdown="company" aria-haspopup="true" aria-expanded="false">
            <span>Company</span>
          </button>
          <a data-analytics-action="pricing" data-analytics-source="global_nav" class="rootLink item-pricing colorize" href="/us/pricing">
            <span>Pricing</span>
          </a>
        </li>

        <li class="navSection secondary">
            <a class="rootLink item-support colorize" href="https://support.stripe.com" data-analytics-action="support" data-analytics-source="global_nav">
              <span>Support</span>
            </a>
          <a class="rootLink item-dashboard colorize" data-adroll-segment="submit_two" href="https://dashboard.stripe.com/login" data-analytics-source="global_nav" data-analytics-action="sign_in">
              <span>Sign in</span>
          </a>

        </li>


        <li class="navSection mobile">
  <a class="rootLink item-mobileMenu colorize"><h2>Menu</h2></a>
  <div class="popup">
    <div class="popupContainer">
      <a class="popupCloseButton">Close</a>
      <div class="mobileProducts">
        <h4>Products</h4>
        <div class="mobileProductsList">
          <ul>
            <li>
              <a class="linkContainer item-payments" href="/us/payments" data-analytics-action="payments" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#87BBFD" class="hover-fillLight" d="M24 48C12.11 48 2.244 39.35.338 28H6.5V9H5.27C9.67 3.515 16.423 0 24 0c13.255 0 24 10.745 24 24S37.255 48 24 48z"/><path fill="#555ABF" class="hover-fillDark" d="M25 21v8H.526A24.082 24.082 0 0 1 0 24 23.908 23.908 0 0 1 6.116 8H31.5c.828 0 1.5.67 1.5 1.5V21h-8zm-10.502-8.995a6.497 6.497 0 1 0 0 12.994 6.497 6.497 0 0 0 0-12.996z"/><path fill="#FFF" d="M39.823 39.276a2.44 2.44 0 0 1-1.76.724H16.5a1.5 1.5 0 0 1-1.5-1.5v-18c0-.828.67-1.5 1.5-1.5h27.693a1.51 1.51 0 0 1 1.484 1.256c.21 1.217.323 2.467.323 3.744 0 5.936-2.355 11.32-6.177 15.276zM33.5 23.002a6.497 6.497 0 1 0 0 12.995 6.497 6.497 0 0 0 .002-12.994z"/></svg>Payments
              </a>
            </li>
            <li>
              <a class="linkContainer item-subscriptions" href="/us/billing" data-analytics-action="subscriptions" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#74E4A2" class="hover-fillLight" d="M24 0c13.255 0 24 10.745 24 24S37.255 48 24 48 0 37.255 0 24 10.745 0 24 0z"/><path fill="#FFF" d="M39.558 30.977c-6.23 6.225-16.304 6.194-22.535-.03l13.975-13.962c-6.232-6.224-16.335-6.224-22.567 0-4.043 4.04-5.456 9.712-4.247 14.896l-.654.174a21.89 21.89 0 0 1-1.536-8.61c.284-11.806 10.003-21.35 21.823-21.446 6.15-.05 11.72 2.42 15.744 6.438 6.23 6.226 6.23 16.318 0 22.542z"/><path fill="#159570" class="hover-fillDark" d="M33.653 21.413c1.43 5.336-1.735 10.82-7.068 12.25-5.332 1.43-10.814-1.736-12.242-7.072-1.43-5.334 1.735-10.82 7.068-12.25 5.334-1.43 10.815 1.738 12.244 7.074z"/></svg>Billing
              </a>
            </li>
            <li>
              <a class="linkContainer item-connect" href="/connect" data-analytics-action="connect" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#68D4F8" class="hover-fillLight" d="M48 24c0 13.255-10.745 24-24 24S0 37.255 0 24 10.745 0 24 0c1.363 0 2.698.12 4 .338V15h5v5h14.662c.218 1.302.338 2.637.338 4z"/><path fill="#FFF" d="M16.99 29.966L17 17l-5.55-.006a1.02 1.02 0 0 0-.725.3L2.65 25.446a1.55 1.55 0 0 0-.44 1.28c1.22 9.944 9.1 17.825 19.042 19.047.472.058.945-.104 1.28-.44l8.172-8.076c.192-.193.3-.453.3-.725L31 31l-12.985-.01a1.023 1.023 0 0 1-1.024-1.024z"/><path fill="#217AB7" class="hover-fillDark" d="M47.697 20.195L37.194 30.702a1.03 1.03 0 0 1-.726.3h-5.462V18.03c0-.567-.46-1.025-1.025-1.025H16.994V11.52c0-.274.108-.534.3-.726L27.783.3C38 1.916 46.07 9.98 47.698 20.194z"/></svg>Connect
              </a>
            </li>
            <li>
              <a class="linkContainer item-sigma" href="/us/sigma" data-analytics-action="sigma" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path class="hover-fillLight" d="M24 48c-2.6 0-5-.3-7.2-1.1V35.2H4v2.1c-2.6-4-4-8.6-4-13.3C0 12.6 7.8 3.2 18.4.6V4h14.4V1.6C41.8 5.1 48 13.8 48 24c0 13.3-10.7 24-24 24z" fill="#beb0f4"/><path class="hover-fillDark" d="M45.6 24H32.8v17.6H17.6v-.2 5.8c-6.4-1.8-11.7-6.1-14.9-12 2.1-6.6 8-10.9 14.9-11.2V.8C19.7.3 21.9 0 24 0c3.4 0 6.7.6 9.6 1.9v8c0 6.1 4.5 10.9 10.2 11.7 1 .2 1.8 1.3 1.8 2.4z" fill="#7356b6"/><path d="M45.6 24c0 1.1-.8 2.1-1.8 2.2-5.8 1-10.2 5.8-10.2 11.7v5.3c-3 1.4-6.2 2.2-9.6 2.2-2.2 0-4.3-.3-6.4-1V40c0-7 5.8-13 12.5-13.8C31.2 26 32 25.1 32 24h13.6zM4 15.7C6.6 9.8 11.5 5.3 17.6 3.4V8c0 7 5.8 12.8 12.5 13.8 1.1.2 1.9 1.1 1.9 2.2H17.9C12 24 6.7 20.6 4 15.7z" fill="#FFF"/></svg>Sigma
              </a>
            </li>
          </ul>
          <ul>
            <li>
              <a class="linkContainer item-atlas" href="/atlas" data-analytics-action="atlas" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#FCD669" class="hover-fillLight" d="M24 0c13.255 0 24 10.745 24 24S37.255 48 24 48 0 37.255 0 24 10.745 0 24 0z"/><path fill="#CE7C3A" class="hover-fillDark" d="M24.012 1.834c.366.005.73.196.92.575l16.825 33.72c.396.79-.314 1.685-1.175 1.48L24 33.626V1.834h.01z"/><path fill="#FFF" d="M24 1.834v31.794l-16.584 3.98A1.043 1.043 0 0 1 6.24 36.13L23.067 2.41c.195-.39.572-.58.947-.576H24z"/></svg>Atlas
              </a>
            </li>
            <li>
              <a class="linkContainer item-radar" href="/us/radar" data-analytics-action="radar" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path class="hover-fillLight" fill="#F6A4EB" d="M41.364 21.886h6.538c.06.697.098 1.4.098 2.114 0 13.255-10.745 24-24 24S0 37.255 0 24 10.745 0 24 0c6.833 0 12.993 2.86 17.364 7.442v14.444z"/><path fill="#FFF" d="M37.746 37.4a1.3 1.3 0 0 1 .92-.38c.72 0 1.303.444 1.303 1.163 0 .503-.353.982-.708 1.292-3.484 3.122-8.325 5.53-13.783 5.53-11.75 0-19.486-9.538-19.486-18.83 0-8.72 7.195-16.19 15.25-16.19s11.227 5.54 11.227 5.54L37.747 37.4z"/><path class="hover-fillDark" fill="#9251AC" d="M47.995 24zm0 0c0-.995-.807-1.974-1.802-1.974-1.15 0-1.8.94-1.8 1.83-.09 3.174-1.228 7.127-3.453 10.182-2.355 3.232-6.91 6.956-13.242 6.956-7.625 0-13.213-5.767-13.213-11.925 0-4.3 2.886-7.17 5.828-7.17 1.588 0 2.48.683 2.965 1.312.362.468 1.063.493 1.482.074L40.968 7.032A23.926 23.926 0 0 1 47.995 24z"/></svg>Radar
              </a>
            </li>
            <li>
              <a class="linkContainer item-issuing" href="/issuing" data-analytics-action="issuing" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><g fill="none"><circle class="hover-fillLight" fill="#87BBFD" cx="24" cy="24" r="24"/><path fill="#FFF" d="M38.27 8H20a4 4 0 0 0-4 4v3H4.59a1 1 0 0 0-.93.61 22.5 22.5 0 0 0-1.44 5.27 1 1 0 0 0 1 1.12H16v14a4 4 0 0 0 4 4h18.27a2 2 0 0 0 1.41-.58 22 22 0 0 0 0-30.84A2 2 0 0 0 38.27 8z"/><path class="hover-fillDark" fill="#555ABF" d="M46.25 15H16v7h31.91c-.2-2.4-.75-4.76-1.66-7z"/></g></svg>Issuing
                <span class="new-badge">New</span>
              </a>
            </li>
            <li>
              <a class="linkContainer item-terminal" href="/terminal" data-analytics-action="terminal" data-analytics-source="mobile_nav">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path class="hover-fillLight" d="M38,8H10L.19,27a24,24,0,0,0,47.62,0Z" fill="#87bbfd"/><path d="M10,24V39.48A3,3,0,0,0,11.29,42a22,22,0,0,0,25.42,0A3,3,0,0,0,38,39.48V24Z" fill="#fff"/><path class="hover-fillDark" d="M24,0A24,24,0,0,0,.19,27H47.81A24,24,0,0,0,24,0ZM38,21H10V14a4,4,0,0,1,4-4H34a4,4,0,0,1,4,4Z" fill="#555abf"/></svg>Terminal
                <span class="new-badge">New</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="mobileSecondaryNav">
        <ul>
          <li>
            <a class="item-pricing" href="/us/pricing" data-analytics-action="pricing" data-analytics-source="mobile_nav">
              Pricing
            </a>
          </li>
            <li>
              <a class="item-workswith" href="/works-with" data-analytics-action="works-with" data-analytics-source="mobile_nav">
                Works with Stripe
              </a>
            </li>
          <li>
            <a class="item-partner-program" href="/partner-program" data-analytics-action="partner-program" data-analytics-source="mobile_nav">
              Partner Program
            </a>
          </li>
          <li>
            <a class="item-documentation" href="/docs" data-analytics-source="mobile_nav" data-analytics-action="documentation">
              Documentation
            </a>
          </li>
        </ul>
        <ul>
          <li>
            <a class="item-about" href="/about" data-analytics-source="mobile_nav" data-analytics-action="about">
              About Stripe
            </a>
          </li>
          <li>
            <a class="item-jobs" href="/jobs" data-analytics-source="mobile_nav" data-analytics-action="jobs">
              Jobs
            </a>
          </li>
          <li>
            <a class="item-newsroom" href="/newsroom" data-analytics-action="newsroom" data-analytics-source="mobile_nav">
              Newsroom
            </a>
          </li>
          <li>
            <a class="item-blog" href="/blog" data-analytics-source="mobile_nav" data-analytics-action="blog">
              Blog
            </a>
          </li>
        </ul>
      </div>
      <a class="mobileSignIn" data-adroll-segment="submit_two" href="https://dashboard.stripe.com/login" data-analytics-source="mobile_nav" data-analytics-action="sign_in">
          Sign in
      </a>
    </div>
  </div>
</li>


      </ul>
      </nav>
  </div>



  <div class="dropdownRoot">
    <div class="dropdownBackground">
      <div class="alternateBackground"></div>
    </div>
    <div class="dropdownArrow"></div>
    <div class="dropdownContainer">

      <div class="dropdownSection" data-dropdown="products" aria-hidden="true">
        <div class="dropdownContent">

          <div class="linkGroup">
            <ul class="productsGroupPrimary">
              <li>
                <a class="linkContainer item-payments" href="/us/payments" data-analytics-action="payments" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#87BBFD" class="hover-fillLight" d="M24 48C12.11 48 2.244 39.35.338 28H6.5V9H5.27C9.67 3.515 16.423 0 24 0c13.255 0 24 10.745 24 24S37.255 48 24 48z"/><path fill="#555ABF" class="hover-fillDark" d="M25 21v8H.526A24.082 24.082 0 0 1 0 24 23.908 23.908 0 0 1 6.116 8H31.5c.828 0 1.5.67 1.5 1.5V21h-8zm-10.502-8.995a6.497 6.497 0 1 0 0 12.994 6.497 6.497 0 0 0 0-12.996z"/><path fill="#FFF" d="M39.823 39.276a2.44 2.44 0 0 1-1.76.724H16.5a1.5 1.5 0 0 1-1.5-1.5v-18c0-.828.67-1.5 1.5-1.5h27.693a1.51 1.51 0 0 1 1.484 1.256c.21 1.217.323 2.467.323 3.744 0 5.936-2.355 11.32-6.177 15.276zM33.5 23.002a6.497 6.497 0 1 0 0 12.995 6.497 6.497 0 0 0 .002-12.994z"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Payments</h3>
                    <p class="linkSub">A complete payments platform engineered for growth.</p>
                  </div>
                </a>
              </li>
              <li>
                <a class="linkContainer item-subscriptions" href="/us/billing" data-analytics-action="billing" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#74E4A2" class="hover-fillLight" d="M24 0c13.255 0 24 10.745 24 24S37.255 48 24 48 0 37.255 0 24 10.745 0 24 0z"/><path fill="#FFF" d="M39.558 30.977c-6.23 6.225-16.304 6.194-22.535-.03l13.975-13.962c-6.232-6.224-16.335-6.224-22.567 0-4.043 4.04-5.456 9.712-4.247 14.896l-.654.174a21.89 21.89 0 0 1-1.536-8.61c.284-11.806 10.003-21.35 21.823-21.446 6.15-.05 11.72 2.42 15.744 6.438 6.23 6.226 6.23 16.318 0 22.542z"/><path fill="#159570" class="hover-fillDark" d="M33.653 21.413c1.43 5.336-1.735 10.82-7.068 12.25-5.332 1.43-10.814-1.736-12.242-7.072-1.43-5.334 1.735-10.82 7.068-12.25 5.334-1.43 10.815 1.738 12.244 7.074z"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Billing</h3>
                    <p class="linkSub">Build and scale your recurring business model.</p>
                  </div>
                </a>
              </li>
              <li>
                <a class="linkContainer item-connect" href="/connect" data-analytics-action="connect" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#68D4F8" class="hover-fillLight" d="M48 24c0 13.255-10.745 24-24 24S0 37.255 0 24 10.745 0 24 0c1.363 0 2.698.12 4 .338V15h5v5h14.662c.218 1.302.338 2.637.338 4z"/><path fill="#FFF" d="M16.99 29.966L17 17l-5.55-.006a1.02 1.02 0 0 0-.725.3L2.65 25.446a1.55 1.55 0 0 0-.44 1.28c1.22 9.944 9.1 17.825 19.042 19.047.472.058.945-.104 1.28-.44l8.172-8.076c.192-.193.3-.453.3-.725L31 31l-12.985-.01a1.023 1.023 0 0 1-1.024-1.024z"/><path fill="#217AB7" class="hover-fillDark" d="M47.697 20.195L37.194 30.702a1.03 1.03 0 0 1-.726.3h-5.462V18.03c0-.567-.46-1.025-1.025-1.025H16.994V11.52c0-.274.108-.534.3-.726L27.783.3C38 1.916 46.07 9.98 47.698 20.194z"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Connect</h3>
                    <p class="linkSub">Everything platforms need to get sellers paid.</p>
                  </div>
                </a>
              </li>
            </ul>
          </div>

          <div class="linkGroup">
            <ul class="productsGroupSecondary">
              <li>
                <a class="linkContainer item-sigma" href="/us/sigma" data-analytics-action="sigma" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path class="hover-fillLight" d="M24 48c-2.6 0-5-.3-7.2-1.1V35.2H4v2.1c-2.6-4-4-8.6-4-13.3C0 12.6 7.8 3.2 18.4.6V4h14.4V1.6C41.8 5.1 48 13.8 48 24c0 13.3-10.7 24-24 24z" fill="#beb0f4"/><path class="hover-fillDark" d="M45.6 24H32.8v17.6H17.6v-.2 5.8c-6.4-1.8-11.7-6.1-14.9-12 2.1-6.6 8-10.9 14.9-11.2V.8C19.7.3 21.9 0 24 0c3.4 0 6.7.6 9.6 1.9v8c0 6.1 4.5 10.9 10.2 11.7 1 .2 1.8 1.3 1.8 2.4z" fill="#7356b6"/><path d="M45.6 24c0 1.1-.8 2.1-1.8 2.2-5.8 1-10.2 5.8-10.2 11.7v5.3c-3 1.4-6.2 2.2-9.6 2.2-2.2 0-4.3-.3-6.4-1V40c0-7 5.8-13 12.5-13.8C31.2 26 32 25.1 32 24h13.6zM4 15.7C6.6 9.8 11.5 5.3 17.6 3.4V8c0 7 5.8 12.8 12.5 13.8 1.1.2 1.9 1.1 1.9 2.2H17.9C12 24 6.7 20.6 4 15.7z" fill="#FFF"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Sigma</h3>
                    <p class="linkSub">Your business data at your fingertips.</p>
                  </div>
                </a>
              </li>
              <li>
                <a class="linkContainer item-atlas" href="/atlas" data-analytics-action="atlas" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#FCD669" class="hover-fillLight" d="M24 0c13.255 0 24 10.745 24 24S37.255 48 24 48 0 37.255 0 24 10.745 0 24 0z"/><path fill="#CE7C3A" class="hover-fillDark" d="M24.012 1.834c.366.005.73.196.92.575l16.825 33.72c.396.79-.314 1.685-1.175 1.48L24 33.626V1.834h.01z"/><path fill="#FFF" d="M24 1.834v31.794l-16.584 3.98A1.043 1.043 0 0 1 6.24 36.13L23.067 2.41c.195-.39.572-.58.947-.576H24z"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Atlas</h3>
                    <p class="linkSub">The best way to start an internet business.</p>
                  </div>
                </a>
              </li>
              <li>
                <a class="linkContainer item-radar" href="/us/radar" data-analytics-action="radar" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path class="hover-fillLight" fill="#F6A4EB" d="M41.364 21.886h6.538c.06.697.098 1.4.098 2.114 0 13.255-10.745 24-24 24S0 37.255 0 24 10.745 0 24 0c6.833 0 12.993 2.86 17.364 7.442v14.444z"/><path fill="#FFF" d="M37.746 37.4a1.3 1.3 0 0 1 .92-.38c.72 0 1.303.444 1.303 1.163 0 .503-.353.982-.708 1.292-3.484 3.122-8.325 5.53-13.783 5.53-11.75 0-19.486-9.538-19.486-18.83 0-8.72 7.195-16.19 15.25-16.19s11.227 5.54 11.227 5.54L37.747 37.4z"/><path class="hover-fillDark" fill="#9251AC" d="M47.995 24zm0 0c0-.995-.807-1.974-1.802-1.974-1.15 0-1.8.94-1.8 1.83-.09 3.174-1.228 7.127-3.453 10.182-2.355 3.232-6.91 6.956-13.242 6.956-7.625 0-13.213-5.767-13.213-11.925 0-4.3 2.886-7.17 5.828-7.17 1.588 0 2.48.683 2.965 1.312.362.468 1.063.493 1.482.074L40.968 7.032A23.926 23.926 0 0 1 47.995 24z"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Radar</h3>
                    <p class="linkSub">Fight fraud with machine learning.</p>
                  </div>
                </a>
              </li>
              <li>
                <a class="linkContainer item-issuing" href="/issuing" data-analytics-action="issuing" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><g fill="none"><circle class="hover-fillLight" fill="#87BBFD" cx="24" cy="24" r="24"/><path fill="#FFF" d="M38.27 8H20a4 4 0 0 0-4 4v3H4.59a1 1 0 0 0-.93.61 22.5 22.5 0 0 0-1.44 5.27 1 1 0 0 0 1 1.12H16v14a4 4 0 0 0 4 4h18.27a2 2 0 0 0 1.41-.58 22 22 0 0 0 0-30.84A2 2 0 0 0 38.27 8z"/><path class="hover-fillDark" fill="#555ABF" d="M46.25 15H16v7h31.91c-.2-2.4-.75-4.76-1.66-7z"/></g></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Issuing<span class="new-badge">New</span></h3>
                    <p class="linkSub">Create, distribute, and manage cards.</p>
                  </div>
                </a>
              </li>
              <li>
                <a class="linkContainer item-terminal" href="/terminal" data-analytics-action="terminal" data-analytics-source="nav_dropdown" tabindex="-1">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path class="hover-fillLight" d="M38,8H10L.19,27a24,24,0,0,0,47.62,0Z" fill="#87bbfd"/><path d="M10,24V39.48A3,3,0,0,0,11.29,42a22,22,0,0,0,25.42,0A3,3,0,0,0,38,39.48V24Z" fill="#fff"/><path class="hover-fillDark" d="M24,0A24,24,0,0,0,.19,27H47.81A24,24,0,0,0,24,0ZM38,21H10V14a4,4,0,0,1,4-4H34a4,4,0,0,1,4,4Z" fill="#555abf"/></svg>
                  <div class="productLinkContent">
                    <h3 class="linkTitle">Terminal<span class="new-badge">New</span></h3>
                    <p class="linkSub">The programmable point of sale.</p>
                  </div>
                </a>
              </li>
            </ul>
          </div>

            <ul class="linkGroup linkList prodsubGroup">
              <li>
                <a class="linkContainer item-workswith" href="/works-with" data-analytics-action="works-with" data-analytics-source="nav_dropdown" tabindex="-1">
                  <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path class="hover-fillLight" fill="#87BBFD" d="M15.998 12.495a1.03 1.03 0 0 1-.595.908L8.93 16.395a1.018 1.018 0 0 1-.86 0l-6.473-2.992a1.03 1.03 0 0 1-.594-.908V4.51c.006-.2.07-.39.18-.55L8.5 7.338l7.32-3.38c.108.16.172.35.178.55v7.984z"/><path class="hover-fillDark" fill="#6772E5" d="M15.998 12.495a1.03 1.03 0 0 1-.595.908L8.93 16.395a1.026 1.026 0 0 1-.43.095V7.34l7.32-3.38c.11.16.173.35.18.55v7.984z"/><path class="hover-fillLight" fill="#87BBFD" d="M8.5 5C6.567 5 5 4.228 5 3.275v-1.15h.098c.36.768 1.742 1.34 3.402 1.34 1.66.002 3.043-.572 3.402-1.34H12v1.15C12 4.228 10.433 5 8.5 5z"/></svg>Works with Stripe</h3>
                </a>
              </li>
            </ul>

        </div>
      </div>

      <div class="dropdownSection" data-dropdown="developers" aria-hidden="true">
        <div class="dropdownContent">

          <div class="linkGroup documentationGroup">
            <a class="linkContainer withIcon item-documentation" href="/docs" data-analytics-action="documentation" data-analytics-source="nav_dropdown" tabindex="-1">
              <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path fill="#87BBFD" class="hover-fillLight" d="M.945 1.998h3.632C6.744 1.998 8.5 3.005 8.5 4.83v11.583c-.512 0-1.015-.337-1.33-.59-1.03-.828-3.057-.828-5.222-.828H.945A.944.944 0 0 1 0 14.052V2.944C0 2.422.423 2 .945 2z"/><path fill="#6772E5" class="hover-fillDark" d="M16.055 1.998h-3.632C10.257 1.998 8.5 3.005 8.5 4.83v11.583c.512 0 1.015-.337 1.33-.59 1.03-.828 3.057-.828 5.222-.828h1.003A.944.944 0 0 0 17 14.05V2.945A.944.944 0 0 0 16.055 2z"/></svg>Documentation</h3>
              <span class="linkSub">Start integrating Stripe’s products and tools.</span>
            </a>
            <div class="documentationArticles">
              <ul>
                <li><h4>Get started</h4></li>
                <li>
                  <a href="/docs/stripe-js/elements/quickstart" data-analytics-action="docs_elements" data-analytics-source="nav_dropdown" tabindex="-1">
                    Elements
                  </a>
                </li>
                <li>
                  <a href="/docs/quickstart" data-analytics-action="docs_checkout_tutorial" data-analytics-source="nav_dropdown" tabindex="-1">
                    Checkout
                  </a>
                </li>
                <li>
                  <a href="/docs/mobile" data-analytics-action="docs_mobile" data-analytics-source="nav_dropdown" tabindex="-1">
                    Mobile apps
                  </a>
                </li>
                <li>
                  <a href="/docs/libraries" data-analytics-action="docs_libraries" data-analytics-source="nav_dropdown" tabindex="-1">
                    Libraries
                  </a>
                </li>
              </ul>
              <ul>
                <li><h4>Popular topics</h4></li>
                <li>
                  <a href="/docs/apple-pay" data-analytics-action="docs_apple_pay" data-analytics-source="nav_dropdown" tabindex="-1">
                    Apple Pay
                  </a>
                </li>
                <li>
                  <a href="/docs/testing" data-analytics-action="docs_testing" data-analytics-source="nav_dropdown" tabindex="-1">
                    Testing
                  </a>
                </li>
                <li>
                  <a href="/docs/checklist" data-analytics-action="docs_launch_checklist" data-analytics-source="nav_dropdown" tabindex="-1">
                    Launch checklist
                  </a>
                </li>
                <li>
                  <a href="/docs/libraries#third-party-plugins" data-analytics-action="docs_plugins" data-analytics-source="nav_dropdown" tabindex="-1">
                    Plug-ins
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <ul class="linkGroup linkList developersGroup">
            <li>
              <a class="linkContainer item-apiReference" href="/docs/api" data-analytics-action="api_reference" data-analytics-source="nav_dropdown" tabindex="-1">
                <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path d="M2 15h13M2 11h13M2 7h13M2 3h13" fill="none" stroke="#6772e5" class="hover-strokeDark" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Full API Reference</h3>
              </a>
            </li>
            <li>
              <a class="linkContainer item-apiStatus" href="https://status.stripe.com" data-analytics-action="api_status" data-analytics-source="nav_dropdown" tabindex="-1">
                <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path d="M1 9h2.95l3-6.5 3 12 3-5.45L16 9" fill="none" stroke="#6772e5" class="hover-strokeDark" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>API Status</h3>
              </a>
            </li>
            <li>
              <a class="linkContainer item-openSource" href="/open-source" data-analytics-action="open_source" data-analytics-source="nav_dropdown" tabindex="-1">
              <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path fill="#6772E5" class="hover-fillDark" d="M8.5 17a8.5 8.5 0 1 1 0-17 8.5 8.5 0 0 1 0 17zM6.987 6.078a.684.684 0 0 0-.968-.968L3.116 8.012a.684.684 0 0 0 0 .967l2.9 2.9a.684.684 0 0 0 .97-.967l-2.42-2.418 2.42-2.42zm6.996 1.95L11.08 5.123a.684.684 0 0 0-.966.968l2.418 2.42-2.418 2.417a.684.684 0 0 0 .967.967l2.904-2.902a.684.684 0 0 0 0-.966z"/></svg>Open Source</h3>
            </a></li>
          </ul>

        </div>
      </div>

      <div class="dropdownSection" data-dropdown="company" aria-hidden="true">
        <div class="dropdownContent">

          <ul class="linkGroup linkList companyGroup">
            <li>
              <a class="linkContainer item-about" href="/about" data-analytics-action="about" data-analytics-source="nav_dropdown" tabindex="-1">
                <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path fill="#6772E5" class="hover-fillDark" d="M8.5 17a8.5 8.5 0 1 1 0-17 8.5 8.5 0 0 1 0 17zm.178-10.89c.76 0 1.726.278 2.486.69V4.443c-.828-.33-1.656-.502-2.484-.502-2.028 0-3.41 1.06-3.41 2.83 0 2.77 3.8 2.32 3.8 3.513 0 .462-.37.612-.93.612-.827 0-1.867-.366-2.706-.823v2.388c.93.4 1.843.592 2.705.592 2.077 0 3.48-1.027 3.48-2.827 0-2.98-3.82-2.447-3.82-3.572-.003-.39.352-.542.877-.542z"/></svg>About Stripe</h3>
              </a>
            </li>
            <li>
              <a class="linkContainer item-customers" href="/us/customers" data-analytics-action="customers" data-analytics-source="nav_dropdown" tabindex="-1">
              <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path fill="#87BBFD" class="hover-fillLight" d="M2 16a1 1 0 0 1-1-1V9a4 4 0 0 1 8 0v7H2zm3-9a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/><path fill="#6772E5" class="hover-fillDark" d="M15 16H9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h.55a2.5 2.5 0 0 1 4.9 0H15a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1z"/><path fill="#87BBFD" class="hover-fillLight" d="M11 12h2v4h-2v-4z"/></svg>Customers</h3>
            </a></li>
            <li>
              <a class="linkContainer item-partner-program" href="/partner-program" data-analytics-action="partner-program" data-analytics-source="nav_dropdown" tabindex="-1">
              <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"> <path class="hover-fillLight" fill="#87bbfd" d="M4.67 10.94A1.6 1.6 0 0 1 5.9 9.05l10.92-2.32a8.47 8.47 0 0 0-1.28-2.98l-5.1 1.08a1.6 1.6 0 0 1 .66 3.12L.18 10.27a8.47 8.47 0 0 0 1.28 2.99l7.18-1.53a1.6 1.6 0 0 1 .67 3.12L4.34 15.9a8.49 8.49 0 0 0 12.53-5.92l-10.3 2.2a1.6 1.6 0 0 1-1.9-1.24zM7.5 3.82a1.6 1.6 0 0 1 1.23-1.89l3.93-.83A8.49 8.49 0 0 0 .13 7.02L9.4 5.05a1.6 1.6 0 0 1-1.9-1.23z"/> <path class="hover-fillDark" fill="#555abf" d="M7.5 3.82a1.6 1.6 0 0 0 1.9 1.23l1.04-.22 5.1-1.08a8.5 8.5 0 0 0-2.88-2.65l-3.93.83a1.6 1.6 0 0 0-1.22 1.9zm9.32 2.91L5.9 9.05a1.6 1.6 0 1 0 .66 3.12l10.3-2.19a8.47 8.47 0 0 0-.04-3.25z"/> <path fill="#fff" d="M12.33 6.06a1.6 1.6 0 0 0-1.9-1.23l-1.03.22L.13 7.02a8.47 8.47 0 0 0 .05 3.25L11.1 7.95a1.6 1.6 0 0 0 1.23-1.9z"/> <path fill="#fff" d="M9.4 5.05l1.04-.22-1.04.22zm1.13 7.91a1.6 1.6 0 0 0-1.89-1.23l-7.18 1.53a8.5 8.5 0 0 0 2.88 2.64l4.97-1.05a1.6 1.6 0 0 0 1.22-1.9z"/> </svg>Partner Program</h3>
            </a></li>
            <li>
              <a class="linkContainer item-jobs" href="/jobs" data-analytics-action="jobs" data-analytics-source="nav_dropdown" tabindex="-1">
                <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path fill="#6772E5" class="hover-fillDark" d="M1.5 4h14c.828 0 1.5.67 1.5 1.5v8a1.5 1.5 0 0 1-1.5 1.5h-14A1.5 1.5 0 0 1 0 13.5v-8C0 4.67.67 4 1.5 4z"/><path fill="#87BBFD" class="hover-fillLight" d="M13 15V4h2v11h-2zM2 4h2v11H2V4z"/><path fill="#6772E5" class="hover-fillDark" d="M11.5 3.5a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1V4H4v-.5A2.5 2.5 0 0 1 6.5 1h4A2.5 2.5 0 0 1 13 3.5V4h-1.5v-.5z"/></svg>Jobs</h3>
              </a>
            </li>
            <li>
              <a class="linkContainer item-environment" href="/environment" data-analytics-action="environment" data-analytics-source="nav_dropdown" tabindex="-1">
                <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"><path class="hover-fillLight" fill="#87BBFD" d="M16.17 1.51c-4.33 6.16-7.92 9.65-12.88 11.91-.32-1.3-1.38-6.55 1.27-9.27 2.76-2.82 6.83-1.68 10.73-2.9a.8.8 0 0 1 .88.26z"/><path class="hover-fillDark" fill="#6772E5" d="M1 14.37c.68-.26 1.33-.6 1.92-1.02.11-.05.22-.11.32-.18 4.61-3 8.17-6.06 12.8-11.79.19.15.29.37.28.6-.11 3.38-.57 7.9-3.13 10.52-2.33 2.38-6.84 1.83-8.83 1.45-.89.7-1.88 1.27-2.93 1.67A.66.66 0 0 1 1 14.37z"/></svg>Environment</h3>
              </a>
            </li>
            <li>
              <a class="linkContainer item-newsroom" href="/newsroom" data-analytics-action="newsroom" data-analytics-source="nav_dropdown" tabindex="-1">
                <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="15"><path fill="#87BBFD" class="hover-fillLight" d="M1 2h4.5v11H1.75C.78 13 0 12.22 0 11.25V3a1 1 0 0 1 1-1z"/><path fill="#6772E5" class="hover-fillDark" d="M14 13H2v-.03c1.14-.12 2-1.08 2-2.22V1a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v9a3 3 0 0 1-3 3zm1-11h-4v4h4V2zM6 2v1h3V2H6zm0 3v1h3V5H6zm0 3v1h9V8H6z"/></svg>Newsroom</h3>
              </a>
            </li>
          </ul>

          <div class="linkGroup blogGroup">
            <a class="linkContainer withIcon item-blog" href="/blog" data-analytics-action="blog" data-analytics-source="nav_dropdown" tabindex="-1">
              <h3 class="linkTitle linkIcon"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17">
    <path fill="#6772E5" class="hover-fillDark" d="M4.5.8v6.29a1.5 1.5 0 1 0 1 0V.8L10 8l-2 7H2L0 8 4.5.8z"/>
    <path fill="#87BBFD" class="hover-fillLight" d="M.5 14h9c.28 0 .5.22.5.5v2a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5v-2c0-.28.22-.5.5-.5z"/>
</svg>From the blog</h3>
            </a>
            <ul class="blogPosts">
              <li>
                <a href="/blog/dashboard-updates-dec-2018" tabindex="-1">
                <span class="title ">New Dashboard updates</span>
                
              </a></li>
              <li>
                <a href="/blog/atlas-scaling-eng" tabindex="-1">
                <span class="title ">Stripe Atlas: guide to scaling engineering organizations</span>
                
              </a></li>
              <li>
                <a href="/blog/premium-support" tabindex="-1">
                <span class="title ">Introducing Premium Support</span>
                
              </a></li>
            </ul>
          </div>

        </div>
      </div>

    </div>
  </div>

</header>


    

    <div class="globalContent">
      
<main>
  <header>
    <div id="stripes" aria-hidden="true">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>

    <section id="intro">
      <div class="container-lg">
        <a class="announcement" href="/terminal">
              <span class="new-pill">New</span>
              <span class="message">Introducing Stripe Terminal</span>
            </a>

        <h1>
          The new standard in online payments
        </h1>
        <p class="common-BodyText">
          Stripe is the best software platform for running an internet business. We handle billions of dollars every year for forward-thinking businesses around the world.
        </p>
        <ul>
            <li>
              <a href="https://dashboard.stripe.com/register" class="common-Button" data-analytics-action="home_cta_experiment_v4" data-analytics-source="header_cta">
                Start Now
              </a>
            </li>
            <li>
              <a href="/contact/sales" class="common-Button" data-analytics-action="contact_sales" data-analytics-source="header_cta">
                Contact Sales
              </a>
            </li>
        </ul>
      </div>
    </section>
  </header>

  
<section id="app-illustrations" class="">
  <div class="tablet-landscape">
    <img alt="slack" src="/img/v3/home/app-illustrations/slack.svg" />
  </div>
  <div class="phone-big">
    <img alt="digitalocean" src="/img/v3/home/app-illustrations/digitalocean.svg" />
  </div>
  <div class="phone-small">
    <img alt="lyft" src="/img/v3/home/app-illustrations/lyft.svg" />
  </div>
  <div class="tablet-portrait">
    <img alt="warbyparker" src="/img/v3/home/app-illustrations/warbyparker.svg" />
  </div>
</section>


  <section id="primary">
    <section id="complete-toolkit" class="container-lg">
      <h2 class="common-UppercaseTitle">
        <svg xmlns="http://www.w3.org/2000/svg" class="heading-icon">
          <circle fill="#B9F4BC" cx="33" cy="33" r="33"/>
          <path d="M15.7 45.3c-.7-2-.7-3.3-.7-8v-8.7c0-4.6 0-6 .7-8 .8-2.2 2.7-4 5-5 2-.6 3.3-.6 8-.6h8.7c4.6 0 6 0 8 .7 2.2.8 4 2.7 5 5 .6 2 .6 3.3.6 8v8.7c0 4.6 0 6-.7 8-.8 2.2-2.7 4-5 5-2 .6-3.3.6-8 .6h-8.7c-4.6 0-6 0-8-.7-2.2-.8-4-2.7-5-5z" fill="#6ED69A"/>
          <g>
            <rect fill="rgb(27,185,120)" x="23" y="27" width="20" height="2" rx="1"/>
            <circle fill="#1BB978" cx="39" cy="28" r="4"/>
          </g>
          <g>
            <rect fill="rgb(185,244,188)" x="23" y="37" width="20" height="2" rx="1"/>
            <circle fill="#1BB978" cx="27.000030595459375" cy="38" r="4"/>
          </g>
        </svg>
        <span>
          The complete toolkit for internet business
        </span>
      </h2>
      <p class="common-BodyText">
        Stripe builds the most powerful and flexible tools for internet commerce. Whether you’re creating a subscription service, an on-demand marketplace, an e-commerce store, or a crowdfunding platform, Stripe’s meticulously designed APIs and unmatched functionality help you create the best possible product for your users. Millions of the world’s most innovative technology companies are scaling faster and more efficiently by building their businesses on Stripe.
      </p>
      <a class="common-BodyText common-Link common-Link--arrow" href="/us/customers">
        Discover how businesses use Stripe
      </a>
    </section>

    <section id="developers-first">
      <div id="programming-languages"><img alt="scala" src="/img/v3/home/programming-languages/scala.svg" aria-hidden="true" style="opacity: 2.26266e-09; transform: translateX(82px) translateY(-82px) rotate(717deg);" /><img alt="rust" src="/img/v3/home/programming-languages/rust.svg" aria-hidden="true" style="opacity: 6.22965e-06; transform: translateX(63.9996px) translateY(-86.9995px) rotate(-158.999deg);" /><img alt="scala" src="/img/v3/home/programming-languages/scala.svg" aria-hidden="true" style="opacity: 7.48527e-05; transform: translateX(3.9997px) translateY(-78.8606px) rotate(245.982deg);" /><img alt="rust" src="/img/v3/home/programming-languages/rust.svg" aria-hidden="true" style="opacity: 0.000329127; transform: translateX(36.9878px) translateY(100.2px) rotate(-412.864deg);" /><img alt="fsharp" src="/img/v3/home/programming-languages/fsharp.svg" aria-hidden="true" style="opacity: 0.000998151; transform: translateX(46.9531px) translateY(-45.2509px) rotate(268.731deg);" /><img alt="haskell" src="/img/v3/home/programming-languages/haskell.svg" aria-hidden="true" style="opacity: 0.0023767; transform: translateX(-91.7813px) translateY(58.8598px) rotate(652.446deg);" /><img alt="fsharp" src="/img/v3/home/programming-languages/fsharp.svg" aria-hidden="true" style="opacity: 0.00484584; transform: translateX(-53.7383px) translateY(117.581px) rotate(-335.367deg);" /><img alt="ruby" src="/img/v3/home/programming-languages/ruby.svg" aria-hidden="true" style="opacity: 0.00887027; transform: translateX(-57.4855px) translateY(45.951px) rotate(-25.7694deg);" /><img alt="scheme" src="/img/v3/home/programming-languages/scheme.svg" aria-hidden="true" style="opacity: 0.0147621; transform: translateX(-12.8081px) translateY(74.4591px) rotate(442.372deg);" /><img alt="go" src="/img/v3/home/programming-languages/go.svg" aria-hidden="true" style="opacity: 0.0235209; transform: translateX(68.3535px) translateY(104.483px) rotate(721.618deg);" /><img alt="rust" src="/img/v3/home/programming-languages/rust.svg" aria-hidden="true" style="opacity: 0.0352474; transform: translateX(96.4753px) translateY(-18.3303px) rotate(-73.3212deg);" /><img alt="javascript" src="/img/v3/home/programming-languages/javascript.svg" aria-hidden="true" style="opacity: 0.0508886; transform: translateX(46.5065px) translateY(-49.9485px) rotate(-102.504deg);" /><img alt="python" src="/img/v3/home/programming-languages/python.svg" aria-hidden="true" style="opacity: 0.0720137; transform: translateX(11.1358px) translateY(-100.954px) rotate(-137.342deg);" /><img alt="go" src="/img/v3/home/programming-languages/go.svg" aria-hidden="true" style="opacity: 0.0991013; transform: translateX(36.0359px) translateY(80.8299px) rotate(188.288deg);" /><img alt="scala" src="/img/v3/home/programming-languages/scala.svg" aria-hidden="true" style="opacity: 0.131986; transform: translateX(-82.4613px) translateY(11.2842px) rotate(492.164deg);" /><img alt="python" src="/img/v3/home/programming-languages/python.svg" aria-hidden="true" style="opacity: 0.172445; transform: translateX(-28.1369px) translateY(69.0486px) rotate(71.1698deg);" /><img alt="rust" src="/img/v3/home/programming-languages/rust.svg" aria-hidden="true" style="opacity: 0.221565; transform: translateX(34.2511px) translateY(68.3405px) rotate(508.318deg);" /><img alt="fsharp" src="/img/v3/home/programming-languages/fsharp.svg" aria-hidden="true" style="opacity: 0.280513; transform: translateX(44.6082px) translateY(2.15846px) rotate(-194.981deg);" /><img alt="php" src="/img/v3/home/programming-languages/php.svg" aria-hidden="true" style="opacity: 0.350467; transform: translateX(-1.29907px) translateY(-75.3242px) rotate(240.977deg);" /><img alt="scheme" src="/img/v3/home/programming-languages/scheme.svg" aria-hidden="true" style="opacity: 0.435737; transform: translateX(-25.9561px) translateY(-56.157px) rotate(349.843deg);" /><img alt="python" src="/img/v3/home/programming-languages/python.svg" aria-hidden="true" style="opacity: 0.5323; transform: translateX(-25.2558px) translateY(-51.9864px) rotate(-88.8629deg);" /><img alt="scheme" src="/img/v3/home/programming-languages/scheme.svg" aria-hidden="true" style="opacity: 0.648007; transform: translateX(-31.3274px) translateY(-11.9678px) rotate(107.006deg);" /><img alt="scala" src="/img/v3/home/programming-languages/scala.svg" aria-hidden="true" style="opacity: 0.781633; transform: translateX(19.2163px) translateY(12.4469px) rotate(18.5612deg);" /><img alt="php" src="/img/v3/home/programming-languages/php.svg" aria-hidden="true" style="opacity: 0.929668; transform: translateX(-5.34523px) translateY(6.61121px) rotate(-25.8822deg);" /></div>
      <h2 class="common-UppercaseTitle">
        <svg xmlns="http://www.w3.org/2000/svg" class="heading-icon">
          <circle fill="#B9F4BC" cx="33" cy="33" r="33"/>
          <path d="M38.4 15l1-3h1l1.2 3c.2.2.5.2.7.3l2.2-2.5 1 .4-.2 3.3c.2 0 .3.2.5.4l3-1.5.7.7-1.4 3 .5.5h3.3l.4.8-2.5 2.2c0 .2 0 .5.2.7l3 1v1l-3 1.2-.3.8 2.5 2-.4 1-3.3-.2-.4.7 1.5 2.8-.7.7-3-1.4c0 .2-.4.4-.6.5l.2 3.3-1 .4-2-2.5c-.3 0-.6 0-1 .2l-1 3h-1l-1-3c-.2-.2-.5-.2-.8-.3l-2 2.5-1-.4.2-3.3-.7-.4-2.8 1.5-.7-.7 1.4-3c-.2 0-.4-.4-.5-.6l-3.3.2-.4-1 2.5-2c0-.3 0-.6-.2-1l-3-1v-1l3-1c.2-.2.2-.4.3-.7l-2.5-2.2.4-1 3.3.2c0-.2.2-.3.4-.5l-1.5-3 .7-.7 3 1.4.5-.5v-3.3l.8-.4 2.2 2.5s.5 0 .7-.2z" fill="#6ED69A" transform="rotate(349.21960800000005 40 25)"/>
          <circle fill="#B9F4BC" cx="40" cy="25" r="2"/>
          <path d="M21.6 26.8L19 25l-1.3 1 1.4 3c0 .2-.3.4-.5.6l-3-.8-1 1.4 2.4 2.3-.4.8-3.2.3-.3 1.6 3 1.4v.8l-3 1.4.4 1.6 3.2.3c0 .3.2.5.3.8l-2.4 2.3.8 1.4 3-.8.7.6-1.3 3 1.3 1 2.6-1.8c.3 0 .5.3.8.4l-.3 3.2 1.6.6 2-2.7c.2 0 .5 0 .7.2l1 3h1.5l1-3c0-.2.4-.2.7-.3l2 2.7 1.4-.6-.4-3.2c.3 0 .5-.3.8-.4L37 49l1.3-1-1.4-3c0-.2.3-.4.5-.6l3 .8 1-1.4-2.4-2.3.4-.8 3.2-.3.3-1.6-3-1.4v-.8l3-1.4-.4-1.6-3.2-.3c0-.3-.2-.5-.3-.8l2.4-2.3-.8-1.4-3 .8-.7-.6 1.3-3-1.3-1-2.6 1.8c-.3 0-.5-.3-.8-.4l.3-3.2-1.6-.6-2 2.7c-.2 0-.5 0-.7-.2l-1-3h-1.5l-1 3c0 .2-.4.2-.7.3l-2-2.7-1.4.6.4 3.2c-.3 0-.5.3-.8.4z" fill="#1BB978" transform="rotate(-349.21960800000005 28 37)"/>
          <circle fill="#B9F4BC" cx="28" cy="37" r="3"/>
        </svg>
        Developers first
      </h2>
      <p class="common-BodyText">
        We believe that payments is a problem rooted in code, not finance. We obsessively seek out elegant, composable abstractions that enable robust, scalable, flexible integrations. Because we eliminate needless complexity and extraneous details, you can get up and running with Stripe in just a couple of minutes.
      </p>
      <section id="notebook" class="container-lg">
        <nav style="top: 2px;">
          <select>
            <option value="payments">Payments</option>
            <option value="customers">Customers</option>
            <option value="subscriptions">Subscriptions</option>
            <option value="reporting">Reporting</option>
          </select>
          <span id="api-method-selection" style="transform: translateY(0%);"></span>
          <ul>
            <li>
              <button class="common-BodyText common-Link selected">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13 14"><path fill="#6772E5" fill-rule="evenodd" d="M0 3a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V3zm0 1h13v2H0V4z"/></svg>
                Payments
              </button>
            </li><li>
              <button class="common-BodyText common-Link">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13 14"><path fill="#6772E5" d="M12.5 11.75c0-1.24-2.69-2.25-6-2.25s-6 1-6 2.25c0 .46.37.9 1.01 1.25h9.98c.64-.36 1.01-.79 1.01-1.25zM6.5 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/></svg>
                Customers
              </button>
            </li><li>
              <button class="common-BodyText common-Link">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13 14"><path fill="#6772E5" d="M6.3 6.3l1.4 1.4L11.5 4 7.7.3 6.3 1.7 7.58 3H6.5a5.5 5.5 0 1 0 5.48 5H9.96A3.5 3.5 0 1 1 6.5 5h1.09l-1.3 1.3z"/></svg>
                Subscriptions
              </button>
            </li><li>
              <button class="common-BodyText common-Link">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13 14"><path fill="#6772E5" d="M0 6.5c0-.27.22-.5.5-.5h2c.28 0 .5.23.5.5v6a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-6zm5-5c0-.28.22-.5.5-.5h2c.28 0 .5.23.5.5v11a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-11zm5 2.01a.5.5 0 0 1 .5-.51h2c.28 0 .5.23.5.51v8.98a.5.5 0 0 1-.5.51h-2a.5.5 0 0 1-.5-.51V3.51z"/></svg>
                Reporting
              </button>
          </li></ul>
          <a href="/docs/api" class="common-BodyText common-Link common-Link--arrow">
            Full API reference
          </a>
        </nav>
        <div id="editor" class="runkit">
          <div id="prism" style="display: none;">
            <pre class="  language-javascript"><span class="custom-line-numbers">1
2
3
4
5
6
7
8
9
10</span><code class="  language-javascript"><span class="token comment" spellcheck="true">// Require the Stripe library with a test secret key.</span>
<span class="token keyword">const</span> stripe <span class="token operator">=</span> <span class="token function">require</span><span class="token punctuation">(</span><span class="token string">'stripe'</span><span class="token punctuation">)</span><span class="token punctuation">(</span><span class="token string">'sk_test_BQokikJOvBiI2HlWgH4olfQ2'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment" spellcheck="true">// Create a payment from a test card token.</span>
<span class="token keyword">const</span> charge <span class="token operator">=</span> <span class="token keyword">await</span> stripe<span class="token punctuation">.</span>charges<span class="token punctuation">.</span><span class="token function">create</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
  amount<span class="token punctuation">:</span> <span class="token number">2000</span><span class="token punctuation">,</span>
  currency<span class="token punctuation">:</span> <span class="token string">'usd'</span><span class="token punctuation">,</span>
  source<span class="token punctuation">:</span> <span class="token string">'tok_visa'</span><span class="token punctuation">,</span>
  description<span class="token punctuation">:</span> <span class="token string">'My first payment'</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
          </div>
          <div id="runkit" style="position: relative;"><iframe src="https://runkit.com/e?name=runkit-embed-0&amp;preamble=&amp;location=https%3A%2F%2Fstripe.com%2F&amp;nodeVersion=8.x.x&amp;minHeight=&amp;theme=stripe-light&amp;gutterStyle=inside&amp;usedDeprecatedOptions=%5B%5D&amp;base64source=Ly8gUmVxdWlyZSB0aGUgU3RyaXBlIGxpYnJhcnkgd2l0aCBhIHRlc3Qgc2VjcmV0IGtleS4KY29uc3Qgc3RyaXBlID0gcmVxdWlyZSgnc3RyaXBlJykoJ3NrX3Rlc3RfQlFva2lrSk92QmlJMkhsV2dING9sZlEyJyk7CgovLyBDcmVhdGUgYSBwYXltZW50IGZyb20gYSB0ZXN0IGNhcmQgdG9rZW4uCmNvbnN0IGNoYXJnZSA9IGF3YWl0IHN0cmlwZS5jaGFyZ2VzLmNyZWF0ZSh7CiAgYW1vdW50OiAyMDAwLAogIGN1cnJlbmN5OiAndXNkJywKICBzb3VyY2U6ICd0b2tfdmlzYScsCiAgZGVzY3JpcHRpb246ICdNeSBmaXJzdCBwYXltZW50Jwp9KTsKCi8vIENsaWNrIOKAnOKWtiBydW7igJ0gdG8gdHJ5IHRoaXMgY29kZSBsaXZlIGFuZCBjcmVhdGUgeW91ciBmaXJzdCBwYXltZW50Lg%3D%3D" frameborder="0" name="runkit-embed-0" style="height: 294.667px; width: 100%; padding: 0px; margin: 0px; border: 0px; background-color: transparent;"></iframe></div>
          <div id="runkit-warning"><p></p></div>
        </div>
      </section>
    </section>
  </section>

  <section id="secondary">
    <div class="cols container-lg">
      <section id="always-improving">
        <h2 class="common-UppercaseText">
          <svg xmlns="http://www.w3.org/2000/svg" class="heading-icon">
            <circle fill="#B9F4BC" cx="33" cy="33" r="33"/>
            <path d="M20 24c0-1.7 1-2.3 2.5-1.3l13 8.6c1.4 1 1.4 2.4 0 3.4l-13 8.6c-1.4 1-2.5.4-2.5-1.3V24" fill="rgb(110, 214, 154)" fill-opacity="0.9999980398084708" transform="translate(-0.00007840766117084286 0.00003234316023181805) scale(0.9999990199042355)"/><path d="M20 24c0-1.7 1-2.3 2.5-1.3l13 8.6c1.4 1 1.4 2.4 0 3.4l-13 8.6c-1.4 1-2.5.4-2.5-1.3V24" fill="rgb(19,182,117)" fill-opacity="0.9999980523645047" transform="translate(12.076221080314621)"/>
            
          </svg>
          Always improving
        </h2>
        <p class="common-BodyText">
          Stripe is an always-improving toolchain that gains new features every month. Our world-class engineering team constantly iterates upon every facet of the Stripe stack. And from Apple Pay to Alipay, building on Stripe means you get early access to the latest technologies.
        </p>
        <a class="common-BodyText common-Link common-Link--arrow" href="/us/payments">
          Learn about Stripe's products
        </a>
      </section>

      <section id="global-scale">
        <h2 class="common-UppercaseText">
          <svg xmlns="http://www.w3.org/2000/svg" class="heading-icon">
            <circle fill="#B9F4BC" cx="33" cy="33" r="33"/>
            <rect fill="none" stroke="#6ED69A" stroke-width="2" x="22" y="22" width="22" height="22" rx="1"/>
            <path d="M22.797896641763177,34.80172092946649 C21.297641689249623,33.30146597695293 19.997450474864458,33.80159345320971 19.997450474864458,36.001912143851655 L19.997450474864458,44.00254952513554 C19.997450474864458,45.102549525135544 20.897450474864456,46.00254952513554 21.997450474864458,46.00254952513554 L29.99808785614834,46.00254952513554 C32.19840654679029,46.00254952513554 32.69847028491868,44.702294572621994 31.19827907053351,43.202103358236826 L28.99821533240512,41.002039620108434 L41.002039620108434,28.99821533240512 L43.202103358236826,31.19827907053351 C44.70235831075038,32.69853402304707 46.00254952513554,32.19840654679029 46.00254952513554,29.99808785614834 L46.00254952513554,21.997450474864458 C46.00254952513554,20.897450474864456 45.102549525135544,19.997450474864458 44.00254952513554,19.997450474864458 L36.001912143851655,19.997450474864458 C33.80159345320971,19.997450474864458 33.30152971508132,21.297705427378013 34.80172092946649,22.797896641763177 L37.001720929466494,24.997896641763177 L24.997896641763177,37.001720929466494 L22.797896641763177,34.80172092946649" stroke="#B9F4BC" stroke-width="2" fill="#1BB978"/>
          </svg>
          Global scale
        </h2>
        <p class="common-BodyText">
          We help power millions of businesses in 100+ countries and across nearly every industry. Headquartered in San Francisco, Stripe has 9 global offices and hundreds of people working to help transform how modern businesses are built and run.
        </p>
        <a class="common-BodyText common-Link common-Link--arrow" href="/about">
          More about us
        </a>
      </section>
    </div>
    
<section id="customer-logos">
  <a href="/us/customers" class="container-lg">
    <span class="common-Button common-Button--default">See our customers</span>
    <ul>
      <li><img class="kickstarter" alt="kickstarter" src="/img/v3/home/customer-logos/kickstarter.svg" />
      </li><li><img class="instacart" alt="instacart" src="/img/v3/home/customer-logos/instacart.svg" />
      </li><li><img class="pinterest" alt="pinterest" src="/img/v3/home/customer-logos/pinterest.svg" />
      </li><li><img class="lyft" alt="lyft" src="/img/v3/home/customer-logos/lyft.svg" />
      </li><li><img class="shopify" alt="shopify" src="/img/v3/home/customer-logos/shopify.svg" />
      </li><li><img class="opentable" alt="opentable" src="/img/v3/home/customer-logos/opentable.svg" />
      </li><li><img class="slack" alt="slack" src="/img/v3/home/customer-logos/slack.svg" />
    </li></ul>
  </a>
</section>

  </section>
</main>



    </div>

    <footer class="globalFooter withCards">

  <section class="globalFooterCards">
    <div class="container-xl">
          <a class="common-Link globalFooterCard card-sigma" href="/us/sigma" data-analytics-action="sigma" data-analytics-source="card_link">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130 130">
  <circle class="hover-fillLight" cx="65" cy="65" r="55" fill="#beb0f4"/>
  <path d="M51.2 65h32.1c0-2.4-1.8-4.6-4.3-4.9C63.3 58 51.2 44.5 51.2 28.3V16.6c-14.1 4-25.7 13.9-31.8 26.9-.4 1-.4 2.4.2 3.5 6.3 10.7 18.2 18 31.6 18z" fill="#FFF"/>
  <path d="M83.3 65c0 2.4-1.8 4.6-4.3 4.9-15.7 2.1-27.8 15.6-27.8 31.8v11.8c4.4 1.2 9 2 13.8 2 7.3 0 14.4-1.7 20.8-4.4 1.4-.6 2.1-1.8 2.1-3.4V97.1c0-13.8 10.1-25.2 23.4-27.2 2.4-.3 4.1-2.4 4.1-4.9v-.2l-32.1.2z" fill="#FFF"/>
  <path class="hover-fillDark" d="M115.4 64.8c0-2.4-1.8-4.4-4.1-4.9-13.3-1.8-23.4-13.3-23.4-27V15.1c-7-3.2-14.7-5-22.9-5-4.7 0-9.3.6-13.8 1.7v16.6C51.2 44.6 63.3 58 79 60.2c2.4.3 4.3 2.4 4.3 4.9l32.1-.3c0 .2 0 .2 0 0z" fill="#7356b6"/>
  <path class="hover-fillDark" d="M18.7 84.9c-.9 1.8-1.7 3.7-2.3 5.7 7 13.6 19.7 23.8 34.8 27.8v-16.6C51.2 85.6 63.3 72.2 79 70c2.4-.3 4.3-2.4 4.3-4.9H51.2c-14.2-.1-26.4 8-32.5 19.8z" fill="#7356b6"/>
</svg>
  <h2 class="common-UppercaseText common-Link--arrow">Introducing Sigma</h2>
  <p class="common-BodyText">Use SQL to explore your business’ payments and revenue data, build and run custom reports, get insights, and more.</p>
</a>

  <a class="common-Link globalFooterCard card-documentation" href="/docs" data-analytics-action="documentation" data-analytics-source="card_link">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130 130">
  <path class="hover-fillDark" fill="#9251AC" d="M113 112H61.36c-2.224 0-4.466-1.574-5.27-3.277C54.005 104.313 46.457 102 37 102H5a5 5 0 0 1-5-5V25a5 5 0 0 1 5-5h33c11.045 0 20 4.477 20 10v37h60v40a5 5 0 0 1-5 5z"/>
  <path class="hover-fillLight" fill="#F6A4EB" d="M121.993 93c0 6-12.363 10.997-27.384 10.997h-3.464v.01h-23.61c-1.823 0-5.27.637-6.82 1.627-.59.377-1.285.544-1.893.195a1.632 1.632 0 0 1-.817-1.416l.003-74.91c0-4.14 4.815-7.5 10.755-7.5h10.51c.075-.002.148-.008.224-.008h13.17c8.922 0 20.682-2.238 25.62-5.573 1.587-1.072 3.702-.09 3.702 1.82 0 0 .007 67.756 0 74.756z"/>
  <path stroke="#FFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M80.5 86.5h26m-26-10h26m-26-17h26m-26-10h26m-26-10h26"/>
  <path stroke="#FFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M68.992 78.007l3.516 3.494-3.516 3.496m0-43.99l3.516 3.495-3.516 3.496"/>
</svg>
  <h2 class="common-UppercaseText common-Link--arrow">Explore the docs</h2>
  <p class="common-BodyText">Start building your integration and accept your first payment in minutes. Stripe libraries are available in every language from Ruby to Go.</p>
</a>


    </div>
  </section>

    <article class="globalFooterCTA">
  <div class="container-lg">

    <div class="content">
      <h1 class="title">
        <span class="subtitle">Ready to get started?</span>
        Get in touch or create an account.
      </h1>
    </div>

    <div class="common-ButtonGroup buttons">

        <a class="common-Button common-Button--default" href="https://dashboard.stripe.com/register" data-analytics-action="sign_up" data-analytics-source="footer_cta">
          Create Stripe account
        </a>

        <a href="/contact/sales" class="common-Button" data-analytics-action="contact_sales" data-analytics-source="footer_cta">
          Contact Sales
          
        </a>
    </div>

  </div>
</article>

  
<script type="application/json" id="runkit-notebook-config">{&amp;quot;enabled&amp;quot;:true,&amp;quot;runkitConfig&amp;quot;:{&amp;quot;sources&amp;quot;:{&amp;quot;payments&amp;quot;:&amp;quot;// Require the Stripe library with a test secret key.\nconst stripe = require(&amp;#39;stripe&amp;#39;)(&amp;#39;sk_test_BQokikJOvBiI2HlWgH4olfQ2&amp;#39;);\n\n// Create a payment from a test card token.\nconst charge = await stripe.charges.create({\n  amount: 2000,\n  currency: &amp;#39;usd&amp;#39;,\n  source: &amp;#39;tok_visa&amp;#39;,\n  description: &amp;#39;My first payment&amp;#39;\n});&amp;quot;,&amp;quot;customers&amp;quot;:&amp;quot;// Require the Stripe library with a test secret key.\nconst stripe = require(&amp;#39;stripe&amp;#39;)(&amp;#39;sk_test_BQokikJOvBiI2HlWgH4olfQ2&amp;#39;);\n\n// Save customer details and payment information.\nconst customer = await stripe.customers.create({\n  source: token, // Token retrieved from Elements, Checkout, or native SDKs.\n  email: &amp;#39;john@example.com&amp;#39;\n});\n\n// Charge or refund customers anytime using their saved payment details.\nlet charge = await stripe.charges.create({\n  amount: 7999,\n  currency: &amp;#39;usd&amp;#39;,\n  customer: customer.id\n});\n\ncharge = await stripe.charges.refund(charge.id, {\n  amount: 1000\n});&amp;quot;,&amp;quot;subscriptions&amp;quot;:&amp;quot;// Require the Stripe library with a test secret key.\nconst stripe = require(&amp;#39;stripe&amp;#39;)(&amp;#39;sk_test_BQokikJOvBiI2HlWgH4olfQ2&amp;#39;);\n\n// Create a monthly plan.\nconst plan = await stripe.plans.create({\n  amount: 999,\n  currency: &amp;#39;usd&amp;#39;,\n  interval: &amp;#39;month&amp;#39;,\n  product: {\n    name: &amp;#39;Diamond Performance&amp;#39;\n  }\n});\n\n// Subscribe the customer to the plan while applying a coupon.\nconst subscription = await stripe.subscriptions.create({\n  customer: customer.id,\n  plan: plan.id,\n  coupon: &amp;#39;25OFF&amp;#39;\n});&amp;quot;,&amp;quot;reporting&amp;quot;:&amp;quot;// Require the Stripe library with a test secret key.\nconst stripe = require(&amp;#39;stripe&amp;#39;)(&amp;#39;sk_test_BQokikJOvBiI2HlWgH4olfQ2&amp;#39;);\nconst moment = require(&amp;#39;moment&amp;#39;);\n\n// Fetch the latest transactions from the Stripe account.\nconst transactions = (await stripe.balance.listTransactions({limit: 75})).data;\n\n// Check what was the most recent transaction.\nconst latestTime = moment(transactions[0].created * 1000).fromNow();\nconsole.log(`Latest transaction: ${transactions[0].type}, ${latestTime}`);\n\n// Plot the evolution of the Stripe balance in USD over the latest transactions.\nlet balance = 0;\nplot(transactions.map(txn =\u003E balance += txn.amount / 100));&amp;quot;},&amp;quot;preambles&amp;quot;:{&amp;quot;customers&amp;quot;:&amp;quot;const token = &amp;#39;tok_visa&amp;#39;;\n&amp;quot;,&amp;quot;subscriptions&amp;quot;:&amp;quot;const customer = await require(&amp;#39;stripe&amp;#39;)(&amp;#39;sk_test_BQokikJOvBiI2HlWgH4olfQ2&amp;#39;).customers.create({\n  source: &amp;#39;tok_visa&amp;#39;,\n  description: &amp;#39;John Doe&amp;#39;,\n  email: &amp;#39;john@example.com&amp;#39;\n});\n&amp;quot;,&amp;quot;reporting&amp;quot;:&amp;quot;const plot = require(\&amp;quot;@runkit/me1000/stripe-graph/releases/1.0.0\&amp;quot;)(\&amp;quot;balances\&amp;quot;);\n&amp;quot;},&amp;quot;epilogues&amp;quot;:{&amp;quot;payments&amp;quot;:&amp;quot;\n\n// Click “▶ run” to try this code live and create your first payment.&amp;quot;}}}</script>



  <article class="globalFooterNav">
  <div class="container-lg">

    <ul class="metaNav">

        <li class="select country">
          <a class="rootLink item-country"><svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"><path d="M1.543,7L6,7,5.979,11.462a0.536,0.536,0,0,0,1.016.24l4.941-9.931a0.537,0.537,0,0,0-.72-0.721L1.3,5.985A0.537,0.537,0,0,0,1.543,7Z"/></svg>
United States</a>

          <div class="popup countryPicker">
            <div class="countryList">
              <h4><a href="https://dashboard.stripe.com/login">Sign up instantly</a></h4>
              <div class="columns">
                <ul class="optionList">
                  <li>
                    <a data-country="AU" class="common-FlagIcon common-FlagIcon--au" href="/au"><span>Australia</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="AT" class="common-FlagIcon common-FlagIcon--at" href="/at"><span>Austria</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="BE" class="common-FlagIcon common-FlagIcon--be" href="/be"><span>Belgium</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="CA" class="common-FlagIcon common-FlagIcon--ca" href="/ca"><span>Canada</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="DK" class="common-FlagIcon common-FlagIcon--dk" href="/dk"><span>Denmark</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="FI" class="common-FlagIcon common-FlagIcon--fi" href="/fi"><span>Finland</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="FR" class="common-FlagIcon common-FlagIcon--fr" href="/fr"><span>France</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="DE" class="common-FlagIcon common-FlagIcon--de" href="/de"><span>Germany</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="HK" class="common-FlagIcon common-FlagIcon--hk" href="/hk"><span>Hong Kong</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="IE" class="common-FlagIcon common-FlagIcon--ie" href="/ie"><span>Ireland</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="IT" class="common-FlagIcon common-FlagIcon--it" href="/it"><span>Italy</span><em class="badge">Preview</em>
                    </a>
                  </li>
                  <li>
                    <a data-country="JP" class="common-FlagIcon common-FlagIcon--jp" href="/jp"><span>Japan</span>
                    </a>
                  </li>
                </ul>
                <ul class="optionList">
                  <li>
                    <a data-country="LU" class="common-FlagIcon common-FlagIcon--lu" href="/lu"><span>Luxembourg</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="NL" class="common-FlagIcon common-FlagIcon--nl" href="/nl"><span>Netherlands</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="NZ" class="common-FlagIcon common-FlagIcon--nz" href="/nz"><span>New Zealand</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="NO" class="common-FlagIcon common-FlagIcon--no" href="/no"><span>Norway</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="PT" class="common-FlagIcon common-FlagIcon--pt" href="/pt"><span>Portugal</span><em class="badge">Preview</em>
                    </a>
                  </li>
                  <li>
                    <a data-country="SG" class="common-FlagIcon common-FlagIcon--sg" href="/sg"><span>Singapore</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="ES" class="common-FlagIcon common-FlagIcon--es" href="/es"><span>Spain</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="SE" class="common-FlagIcon common-FlagIcon--se" href="/se"><span>Sweden</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="CH" class="common-FlagIcon common-FlagIcon--ch" href="/ch"><span>Switzerland</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="GB" class="common-FlagIcon common-FlagIcon--gb" href="/gb"><span>United Kingdom</span>
                    </a>
                  </li>
                  <li>
                    <a data-country="US" class="common-FlagIcon common-FlagIcon--us selected" href="/"><span>United States</span>
                    </a>
                  </li>
                </ul>
               </div>
            </div>
            <div class="sidebar">
              <div class="countryList">
                <h4><a href="/global">Request an invite</a></h4>
                <ul class="optionList">
                  <li>
                    <a class="common-FlagIcon common-FlagIcon--br" href="https://stripe.com/global#BR"><span>Brazil</span><em class="badge">Preview</em>
                    </a>
                  </li>
                  <li>
                    <a class="common-FlagIcon common-FlagIcon--mx" href="https://stripe.com/global#MX"><span>Mexico</span><em class="badge">Preview</em>
                    </a>
                  </li>
                </ul>
              </div>
              <a class="globalLink" href="/global">
                <span>More countries coming soon.</span>
                <strong>Sign up to get notified</strong>
              </a>
            </div>
          </div>

        </li>

        <li class="select language">
          <a class="rootLink item-language"><svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"><path d="M8.079,9.837L6.116,12.3A0.654,0.654,0,0,1,5,11.841V9.852C2.488,9.351,1,7.6,1,5.5,1,3.015,3.087,1,6.5,1S12,3.015,12,5.5A4.5,4.5,0,0,1,8.079,9.837Z"/></svg>
English</a>

          <div class="popup languagePicker">
            <ul class="optionList">
              <li>
                <a data-language="de" href="/locale?locale=de&amp;redirect=/" rel="nofollow"><span>Deutsch</span>
                </a>
              </li>
              <li>
                <a data-language="en" href="/locale?locale=en&amp;redirect=/" class="selected" rel="nofollow"><span>English</span>
                </a>
              </li>
              <li>
                <a data-language="es" href="/locale?locale=es&amp;redirect=/" rel="nofollow"><span>Español</span>
                </a>
              </li>
              <li>
                <a data-language="fr" href="/locale?locale=fr&amp;redirect=/" rel="nofollow"><span>Français</span>
                </a>
              </li>
              <li>
                <a data-language="it" href="/locale?locale=it&amp;redirect=/" rel="nofollow"><span>Italiano</span>
                </a>
              </li>
              <li>
                <a data-language="ja" href="/locale?locale=ja&amp;redirect=/" rel="nofollow"><span>日本語</span>
                </a>
              </li>
            </ul>
          </div>

        </li>

      <li class="space"></li>

      <li class="copyright">© Stripe</li>
    </ul>

    <div class="siteNav">
      <div class="column">
        <h4>Products</h4>
        <div class="splitColumn">
          <ul>
            <li><a href="/us/payments"><strong>Payments</strong></a></li>
            <li><a href="/us/billing"><strong>Billing</strong></a></li>
            <li><a href="/connect"><strong>Connect</strong></a></li>
            <li><a href="/us/sigma"><strong>Sigma</strong></a></li>
            <li><a href="/atlas"><strong>Atlas</strong></a></li>
            <li><a href="/us/radar"><strong>Radar</strong></a></li>
            <li><a href="/issuing"><strong>Issuing</strong></a></li>
            <li><a href="/terminal"><strong>Terminal</strong></a></li>
          </ul>
          <ul>
            <li><a href="/us/pricing">Pricing</a></li>
              <li class="long-link"><a href="/works-with">Works with Stripe</a></li>
            <li><a href="/global">Global</a></li>
              <li><a href="/guides">Guides</a></li>
          </ul>
        </div>
      </div>
      <div class="column">
        <h4>Developers</h4>
        <ul>
          <li><a href="/docs">Documentation</a></li>
          <li><a href="/docs/api">API reference</a></li>
          <li><a href="https://status.stripe.com">API status</a></li>
          <li><a href="/open-source">Open source</a></li>
        </ul>
      </div>
      <div class="column">
        <h4>Company</h4>
        <ul>
          <li><a href="/about">About</a></li>
          <li><a href="/us/customers">Customers</a></li>
            <li><a href="/partner-program">Partner Program</a></li>
          <li><a href="/jobs">Jobs</a></li>
          <li><a href="/blog">Blog</a></li>
            <li><a href="/newsroom">Newsroom</a></li>
          <li><a href="/environment">Environment</a></li>
        </ul>
      </div>
      <div class="column">
        <h4>Resources</h4>
        <ul>
          <li>
            <a href="https://support.stripe.com">Support</a>
          </li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/us/privacy">Privacy &amp; terms</a></li>
          <li><a href="/sitemap">Sitemap</a></li>
        </ul>
      </div>
    </div>

  </div>
</article>


</footer>


    <script type="application/json" id="site-feature-flags">
      {"analytics_id_holdback":false,"merchant_token_holdback":false,"contact_sales_content":true,"contact_sales_integration_question":false,"contact_sales_products_and_dev_support":false,"pricing_revamp":true,"growth_home_top_nav_cta":false,"growth_home_jp_sales_cta":true,"docs_api_use_sail":false,"growth_home_cta_v4":true,"growth_welcome_card_v2":true,"growth_home_onboarding_task_list":false}
    </script>

    

    


<script type="application/json" id="site-analytics-config">{&amp;quot;generalAnalyticsConfig&amp;quot;:{&amp;quot;ga&amp;quot;:{},&amp;quot;flags&amp;quot;:{&amp;quot;analytics_id_holdback&amp;quot;:false,&amp;quot;merchant_token_holdback&amp;quot;:false,&amp;quot;contact_sales_content&amp;quot;:true,&amp;quot;contact_sales_integration_question&amp;quot;:false,&amp;quot;contact_sales_products_and_dev_support&amp;quot;:false,&amp;quot;pricing_revamp&amp;quot;:true,&amp;quot;growth_home_top_nav_cta&amp;quot;:false,&amp;quot;growth_home_jp_sales_cta&amp;quot;:true,&amp;quot;docs_api_use_sail&amp;quot;:false,&amp;quot;growth_home_cta_v4&amp;quot;:true,&amp;quot;growth_welcome_card_v2&amp;quot;:true,&amp;quot;growth_home_onboarding_task_list&amp;quot;:false},&amp;quot;locale&amp;quot;:&amp;quot;en&amp;quot;,&amp;quot;treatments&amp;quot;:{&amp;quot;growth_home_top_nav_cta&amp;quot;:0,&amp;quot;growth_home_jp_sales_cta&amp;quot;:0,&amp;quot;growth_welcome_card_v2&amp;quot;:1}},&amp;quot;siteSpecificAnalyticsConfig&amp;quot;:{&amp;quot;pageId&amp;quot;:&amp;quot;home&amp;quot;,&amp;quot;trackPageViewed&amp;quot;:true,&amp;quot;gtmConfig&amp;quot;:{&amp;quot;event&amp;quot;:&amp;quot;dataLayer-initialized&amp;quot;,&amp;quot;user-id&amp;quot;:null,&amp;quot;account-id&amp;quot;:null,&amp;quot;merchant-id&amp;quot;:null,&amp;quot;user-role&amp;quot;:null,&amp;quot;products-enabled&amp;quot;:null,&amp;quot;page-category&amp;quot;:null,&amp;quot;language&amp;quot;:&amp;quot;en&amp;quot;,&amp;quot;country&amp;quot;:&amp;quot;US&amp;quot;,&amp;quot;signed-in&amp;quot;:false,&amp;quot;signup-type&amp;quot;:null}}}</script>

<noscript>&lt;img alt="" height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=742650679237989&amp;ev=PageView&amp;noscript=1" /&gt;</noscript>

<img height="1" width="1" style="display:none;" alt="" src="https://dc.ads.linkedin.com/collect/?pid=332772&amp;fmt=gif" />
<!-- Google Tag Manager (noscript) -->
<noscript>&lt;iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W8NSNKQ"
height="0" width="0" style="display:none;visibility:hidden"&gt;&lt;/iframe&gt;</noscript>
<!-- End Google Tag Manager (noscript) -->


<script src="/assets/compiled/js/site-analytics-8f2f65ac24a2d0c7f862.min.js"></script>
<script defer="" src="https://js.stripe.com/internal/v2/analytics.min.js"></script>
<script defer="" src="https://js.stripe.com/v2/stripe-m-preview.js"></script>

    <div class="cookie-notification-container " rel="cookie-notification">
  <div class="cookie-notification">
      <span class="cookie-notification-copy">
        By using this website you agree to our <a class="common-Link" href="/cookies-policy/legal">cookie policy</a>
      </span>
      <button class="dismiss-button" rel="dismiss-cookie-notification">Close</button>
  </div>
</div>


    <link type="text/css" rel="stylesheet" href="//fast.fonts.net/t/1.css?apiType=css&amp;projectid=4414faae-0f1e-48be-9319-851fc710f613" />

  


<script type="text/javascript" id="">(function(m,n){function p(a){a=e[a].toString()+"%";dataLayer.push({event:"scroll-milestone",milestone:a})}dataLayer=window.dataLayer||[];var q=m,e=n,h=0,k,l=0,f=Math.max,r=Math.round;window.onscroll=function(){var a=window,b=document;var c=a.innerHeight||(b.documentElement?b.documentElement.clientHeight:b.body.clientHeight)||b.body.clientHeight;var d=b.body;var g=b.documentElement;d=b.height||f(f(d.scrollHeight,g.scrollHeight),f(d.offsetHeight,g.offsetHeight),f(d.clientHeight,g.clientHeight));a=a.pageYOffset||
(b.documentElement?b.documentElement.scrollTop:b.body.scrollTop)||b.body.scrollTop;c=d-(c+a);c=c/d*100;c=100-c;for(a=e.length;a;)a--,r(c)&gt;=e[a]&amp;&amp;l&lt;e[a]&amp;&amp;(currentMilestone=l=e[a],currentMilestone!=h&amp;&amp;(h=currentMilestone,window.clearTimeout(k),k=window.setTimeout(p(a),q)),a=0)}})(2E3,[0,25,50,75,100]);</script><script type="text/javascript" id="">ga(function(){var a=ga.getAll()[0].get("name");ga(a+".require","Clearbit",{mapping:{companyDomain:"dimension18",companyEmployeesRange:"dimension19",companyEstimatedAnnualRevenue:"dimension20"}})});</script>

<script type="text/javascript" id="" src="https://ga.clearbit.com/v1/ga.js?authorization=pk_5bf3234405eeb3bec2b2b88bc0ab0280"></script><iframe src="https://js.stripe.com/v2/m/outer.html#referrer=&amp;title=Stripe%20-%20Online%20payment%20processing%20for%20internet%20businesses&amp;url=https%3A%2F%2Fstripe.com%2F&amp;muid=3964cd72-b9bb-4da3-98ad-0247a62c8db8&amp;sid=f7eaa1a0-b1f6-42b7-8629-472de13dd40a&amp;preview=true&amp;" frameborder="0" allowtransparency="true" scrolling="no" tabindex="-1" aria-hidden="true" style="width: 1px !important; height: 1px !important; position: fixed !important; visibility: hidden !important; pointer-events: none !important;"></iframe></body></html>

'''

css = '''

*{-webkit-box-sizing:border-box;box-sizing:border-box}blockquote,body,button,dd,dl,figure,h1,h2,h3,h4,h5,h6,ol,p,pre,ul{margin:0;padding:0}ol,ul{list-style:none}a{text-decoration:none}button,select{border:none;outline:none;background:none;font-family:inherit}a,button,input,select,textarea{-webkit-tap-highlight-color:transparent}:root{overflow-x:hidden;height:100%}body{background:#fff;min-height:100%;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;font-size:62.5%;font-family:Camphor,Open Sans,Segoe UI,sans-serif;font-weight:400;font-style:normal;-webkit-text-size-adjust:100%;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility;-webkit-font-feature-settings:"pnum";font-feature-settings:"pnum";font-variant-numeric:proportional-nums}.globalContent{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}html[lang=ja] body{font-family:Camphor,Meiryo,Hiragino Sans,sans-serif}code,pre{font-family:Source Code Pro,Consolas,Menlo,monospace}@font-face{font-family:StripeIcons;src:url("/fonts/stripe-icons.woff2") format("woff2"),url("/fonts/stripe-icons.woff") format("woff")}@font-face{font-family:Camphor;font-weight:300;src:url("/fonts/camphor-ss/300-light.woff2") format("woff2"),url("/fonts/camphor-ss/300-light.woff") format("woff")}@font-face{font-family:Camphor;font-weight:300;font-style:italic;src:url("/fonts/camphor-ss/300-light-italic.woff2") format("woff2"),url("/fonts/camphor-ss/300-light-italic.woff") format("woff")}@font-face{font-family:Camphor;font-weight:400;src:url("/fonts/camphor-ss/400-regular.woff2") format("woff2"),url("/fonts/camphor-ss/400-regular.woff") format("woff")}@font-face{font-family:Camphor;font-weight:400;font-style:italic;src:url("/fonts/camphor-ss/400-regular-italic.woff2") format("woff2"),url("/fonts/camphor-ss/400-regular-italic.woff") format("woff")}@font-face{font-family:Camphor;font-weight:500;src:url("/fonts/camphor-ss/500-medium.woff2") format("woff2"),url("/fonts/camphor-ss/500-medium.woff") format("woff")}@font-face{font-family:Camphor;font-weight:500;font-style:italic;src:url("/fonts/camphor-ss/500-medium-italic.woff2") format("woff2"),url("/fonts/camphor-ss/500-medium-italic.woff") format("woff")}@font-face{font-family:Camphor;font-weight:600;src:url("/fonts/camphor-ss/600-bold.woff2") format("woff2"),url("/fonts/camphor-ss/600-bold.woff") format("woff")}@font-face{font-family:Camphor;font-weight:600;font-style:italic;src:url("/fonts/camphor-ss/600-bold-italic.woff2") format("woff2"),url("/fonts/camphor-ss/600-bold-italic.woff") format("woff")}@font-face{font-family:Source Code Pro;font-weight:400;src:url("/fonts/sourcecodepro-ss/SourceCodePro-Medium.woff2") format("woff2"),url("/fonts/sourcecodepro-ss/SourceCodePro-Medium.woff") format("woff")}@font-face{font-family:Source Code Pro;font-weight:600;src:url("/fonts/sourcecodepro-ss/SourceCodePro-Bold.woff2") format("woff2"),url("/fonts/sourcecodepro-ss/SourceCodePro-Bold.woff") format("woff")}@font-face{font-family:Flow-Block;src:url("/fonts/flow/flow-block.woff") format("woff")}@font-face{font-family:Flow-Rounded;src:url("/fonts/flow/flow-rounded.woff") format("woff")}@font-face{font-family:Flow-Circular;src:url("/fonts/flow/flow-circular.woff") format("woff")}.container,.container-fluid,.container-lg,.container-wide,.container-xl{margin:0 auto;padding:0 20px;width:100%}.container,.container-lg{max-width:1040px}.container-wide,.container-xl{max-width:1160px}.common-PageTitle{font-weight:300;font-size:45px;line-height:56px;color:#32325d;letter-spacing:-.01em}@media (min-width:670px){.common-PageTitle{font-size:53px;line-height:68px}}.common-SectionTitle{font-weight:400;font-size:34px;line-height:44px;color:#32325d}@media (min-width:670px){.common-SectionTitle{font-size:42px;line-height:52px}}.common-SectionTitleHighlight{font-weight:300;color:#6772e5}.common-IntroText{font-weight:300;font-size:21px;line-height:32px;color:#424770}@media (min-width:670px){.common-IntroText{font-size:24px;line-height:36px}}.common-BodyTitle{font-weight:500;font-size:19px;line-height:32px;color:#32325d}.common-BodyText{font-weight:400;font-size:17px;line-height:28px;color:#525f7f}.common-MediumBodyText{font-weight:400;font-size:19px;line-height:32px;color:#525f7f}.common-UppercaseTitle{font-size:20px;line-height:32px;font-weight:600;text-transform:uppercase;letter-spacing:.025em}@media (min-width:670px){.common-UppercaseTitle{font-size:21px;line-height:32px}}.common-UppercaseText{font-size:17px;line-height:28px;font-weight:600;text-transform:uppercase;letter-spacing:.025em}.common-AlignRight{text-align:right}.common-AlignCenter{text-align:center}.common-NoWrap{white-space:nowrap}.common-ProductLockup,.common-ProductLockupBack{font-size:24px;line-height:30px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}@media (min-width:670px){.common-ProductLockup,.common-ProductLockupBack{font-size:28px;line-height:38px}}.common-ProductLockup .icon,.common-ProductLockupBack .icon{width:64px;height:64px;overflow:hidden;border-radius:50%;-webkit-box-shadow:0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);box-shadow:0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);margin-right:20px}@media (min-width:670px){.common-ProductLockup .icon,.common-ProductLockupBack .icon{width:72px;height:72px}}.common-ProductLockupBack{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;font-size:20px;-webkit-transition:color .1s;transition:color .1s}.common-ProductLockupBack:before{font:normal 48px/24px StripeIcons;content:"\279D";-webkit-transform:scaleX(-1);transform:scaleX(-1);width:36px;text-align:right;position:relative;top:-6px;-webkit-transition:color .1s;transition:color .1s}.common-ProductLockupBack .icon{width:48px;height:48px}.common-ProductLockupBack .hover-fillDark,.common-ProductLockupBack .hover-fillLight{-webkit-transition:fill .1s;transition:fill .1s}.common-ProductLockupBack .hover-strokeDark,.common-ProductLockupBack .hover-strokeLight{-webkit-transition:stroke .1s;transition:stroke .1s}.common-ProductLockupBack:hover .hover-fillLight{fill:#8898aa}.common-ProductLockupBack:hover .hover-fillDark{fill:#32325d}.common-ProductLockupBack:hover .hover-strokeLight{stroke:#8898aa}.common-ProductLockupBack:hover .hover-strokeDark{stroke:#32325d}.common-Link{color:#6772e5;font-weight:500;-webkit-transition:color .1s ease;transition:color .1s ease;cursor:pointer}.keyboard-navigation .common-Link:focus{outline:none;text-decoration:underline;text-underline-position:under}.common-Link:focus,.common-Link:hover{color:#32325d}.common-Link:active{color:#000}.common-Link--arrow:after{font:normal 16px StripeIcons;content:"\2192";padding-left:5px}.common-Link--arrowL:before{content:"\2192";-webkit-transform:rotate(180deg);transform:rotate(180deg);margin-right:5px}.common-Link--arrowL:before,.common-Link--download:before{display:inline-block;font:normal 16px StripeIcons;vertical-align:-2px}.common-Link--download:before{content:"\279C";margin-right:2px;-webkit-transform:rotate(90deg) scale(.9);transform:rotate(90deg) scale(.9)}.common-UppercaseText.common-Link--arrow:after{content:"\279C"}.common-InvertedText .common-BodyTitle,.common-InvertedText .common-PageTitle,.common-InvertedText .common-SectionTitle,.common-InvertedText .common-SectionTitleHighlight,.common-InvertedText .common-UppercaseText,.common-InvertedText .common-UppercaseTitle{color:#fff}.common-InvertedText .common-IntroText{color:#c4f0ff}.common-InvertedText .common-BodyText{color:#9cdbff}.common-InvertedText .common-Link,.common-Link--white{color:#fff}.common-InvertedText .common-Link:focus,.common-InvertedText .common-Link:hover,.common-Link--white:focus,.common-Link--white:hover{color:#c4f0ff}.common-InvertedText .common-Link:active,.common-Link--white:active{color:#87bbfd}.common-Button{white-space:nowrap;display:inline-block;height:40px;line-height:40px;padding:0 14px;-webkit-box-shadow:0 4px 6px rgba(50,50,93,.11),0 1px 3px rgba(0,0,0,.08);box-shadow:0 4px 6px rgba(50,50,93,.11),0 1px 3px rgba(0,0,0,.08);background:#fff;border-radius:4px;font-size:15px;font-weight:600;text-transform:uppercase;letter-spacing:.025em;color:#6772e5;text-decoration:none;-webkit-transition:all .15s ease;transition:all .15s ease}.keyboard-navigation .common-Button:focus{outline:none;-webkit-box-shadow:0 0 0 1.5px hsla(0,0%,100%,.75),0 0 0 1.25px rgba(82,95,127,.5) inset,0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);box-shadow:0 0 0 1.5px hsla(0,0%,100%,.75),inset 0 0 0 1.25px rgba(82,95,127,.5),0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3)}.common-Button:focus,.common-Button:hover{color:#7795f8;-webkit-transform:translateY(-1px);transform:translateY(-1px);-webkit-box-shadow:0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);box-shadow:0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);-webkit-box-shadow:0 7px 14px rgba(50,50,93,.1),0 3px 6px rgba(0,0,0,.08);box-shadow:0 7px 14px rgba(50,50,93,.1),0 3px 6px rgba(0,0,0,.08)}.common-Button:active{color:#555abf;background-color:#f6f9fc;-webkit-transform:translateY(1px);transform:translateY(1px);-webkit-box-shadow:0 6px 12px -2px rgba(50,50,93,.25),0 3px 7px -3px rgba(0,0,0,.3);box-shadow:0 6px 12px -2px rgba(50,50,93,.25),0 3px 7px -3px rgba(0,0,0,.3)}.common-Button--default{color:#fff;background:#6772e5}.common-Button--default:focus,.common-Button--default:hover{color:#fff;background-color:#7795f8}.common-Button--default:active{color:#e6ebf1;background-color:#555abf}.common-Button--dark{color:#fff;background:#32325d}.common-Button--dark:focus,.common-Button--dark:hover{color:#fff;background-color:#43458b}.common-Button--dark:active{color:#e6ebf1;background-color:#32325d}.common-Button--disabled{color:#fff;background:#aab7c4;pointer-events:none}.common-ButtonIcon{display:inline;margin:0 5px 0 0;position:relative}.common-ButtonGroup{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin:-10px}.common-ButtonGroup .common-Button{-ms-flex-negative:0;flex-shrink:0;margin:10px}.StripeBackground{position:absolute;left:0;top:50%;right:0;-webkit-transform:skewY(-12deg);transform:skewY(-12deg);pointer-events:none}.StripeBackground .stripe{position:absolute;top:auto;left:0;right:0}.StripeBackground .stripe.pattern{overflow:hidden}.StripeBackground .stripe.pattern:after{content:"";position:absolute;left:0;right:0;bottom:-1000px;top:-1000px;-webkit-transform:skew(0,12deg);transform:skew(0,12deg)}.common-StripeGrid{--stripe-height:48px;--content-columns:12;--gutter-columns:4;position:absolute;width:100%;top:0;bottom:0;z-index:-1;pointer-events:none}@media (min-width:670px){.common-StripeGrid{--stripe-height:64px}}.common-StripeGrid .backgroundContainer,.common-StripeGrid .stripeContainer{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:center;-ms-flex-align:center;align-items:center;position:absolute;width:100%;height:100%;-webkit-transform:skewY(-12deg);transform:skewY(-12deg)}.common-StripeGrid .backgroundContainer .grid{grid-template-columns:1fr;min-width:0}.common-StripeGrid .backgroundContainer .background{grid-row:1/-1;grid-column:1/-1;z-index:-1}.common-StripeGrid .stripeContainer{overflow:hidden}.common-StripeGrid.anchorBottom .backgroundContainer,.common-StripeGrid.anchorBottom .stripeContainer{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.common-StripeGrid.anchorBottom .grid{height:200%;-ms-flex-line-pack:end;align-content:end}.common-StripeGrid .grid{--content-column-width:minmax(0,calc(1040px / var(--content-columns)));--gutter-column-width:1fr;position:absolute;width:100%;height:100%;display:grid;grid-template-rows:repeat(auto-fill,var(--stripe-height));grid-template-columns:[viewport-start] 1fr [left-gutter-start] repeat(var(--gutter-columns),var(--gutter-column-width)) [left-gutter-end content-start] repeat(var(--content-columns),var(--content-column-width)) [content-end right-gutter-start] repeat(var(--gutter-columns),var(--gutter-column-width)) [right-gutter-end] 1fr [viewport-end]}@media (min-width:1040px){.common-StripeGrid .grid{--gutter-column-width:var(--content-column-width);min-width:calc(1040px / var(--content-columns) * (var(--gutter-columns) * 2 + var(--content-columns)))}}.common-Card{position:relative;background-color:#fff;border-radius:8px;padding:30px;-webkit-box-shadow:0 30px 60px -12px rgba(50,50,93,.25),0 18px 36px -18px rgba(0,0,0,.3);box-shadow:0 30px 60px -12px rgba(50,50,93,.25),0 18px 36px -18px rgba(0,0,0,.3)}@media (min-width:880px){.common-Card{padding:50px}}.common-BetaBadge{display:inline;position:relative;height:18px;margin-left:11px;border-radius:9px;font-size:12px;font-weight:600;text-align:center;padding:2px 6px 2px 7px;text-transform:uppercase;color:#8898aa;background-color:rgba(136,152,170,.15)}.lg-cols,.lg-grid,.lg-rows,.md-cols,.md-grid,.md-rows,.sm-cols,.sm-grid,.sm-rows,.xs-cols,.xs-grid,.xs-rows{display:-webkit-box;display:-ms-flexbox;display:flex;margin:-20px}.feature-block{-webkit-box-flex:1;-ms-flex:1;flex:1;padding:20px;position:relative}.xs-cols{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}.xs-cols .feature-block{-ms-flex-preferred-size:100%;flex-basis:100%}.xs-rows{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.xs-rows .feature-block{-ms-flex-preferred-size:auto;flex-basis:auto}.xs-grid{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-ms-flex-wrap:wrap;flex-wrap:wrap}.xs-grid .feature-block{-ms-flex-preferred-size:50%;flex-basis:50%}@media (min-width:670px){.sm-cols{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}.sm-cols .feature-block{-ms-flex-preferred-size:100%;flex-basis:100%}.sm-rows{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.sm-rows .feature-block{-ms-flex-preferred-size:auto;flex-basis:auto}.sm-grid{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-ms-flex-wrap:wrap;flex-wrap:wrap}.sm-grid .feature-block{-ms-flex-preferred-size:50%;flex-basis:50%}}@media (min-width:880px){.md-cols{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-ms-flex-wrap:nowrap;flex-wrap:nowrap}.md-cols .feature-block{-ms-flex-preferred-size:100%;flex-basis:100%}.md-rows{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-ms-flex-wrap:nowrap;flex-wrap:nowrap}.md-rows .feature-block{-ms-flex-preferred-size:auto;flex-basis:auto}.md-grid{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-ms-flex-wrap:wrap;flex-wrap:wrap}.md-grid .feature-block{-ms-flex-preferred-size:50%;flex-basis:50%}}@media (min-width:1040px){.lg-cols{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-ms-flex-wrap:nowrap;flex-wrap:nowrap}.lg-cols .feature-block{-ms-flex-preferred-size:100%;flex-basis:100%}.lg-rows{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-ms-flex-wrap:nowrap;flex-wrap:nowrap}.lg-rows .feature-block{-ms-flex-preferred-size:auto;flex-basis:auto}.lg-grid{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-ms-flex-wrap:wrap;flex-wrap:wrap}.lg-grid .feature-block{-ms-flex-preferred-size:50%;flex-basis:50%}}.xs-icon-top .icon{margin:10px 0 20px -3px}.xs-icon-left{padding-left:50px}.xs-icon-left .icon{position:absolute;left:-24px;top:7px}@media (min-width:670px){.sm-icon-top{padding-left:0}.sm-icon-top .icon{position:static;margin:10px 0 20px -3px}.sm-icon-left{padding-left:50px}.sm-icon-left .icon{position:absolute;left:-24px;top:7px}}@media (min-width:880px){.md-icon-top{padding-left:0}.md-icon-top .icon{position:static;margin:10px 0 20px -3px}.md-icon-left{padding-left:50px}.md-icon-left .icon{position:absolute;left:-24px;top:7px}}@media (min-width:1040px){.lg-icon-top{padding-left:0}.lg-icon-top .icon{position:static;margin:10px 0 20px -3px}.lg-icon-left{padding-left:50px}.lg-icon-left .icon{position:absolute;left:-24px;top:7px}}.feature-block h3,.feature-block p{margin-bottom:10px}.feature-block h3:last-child,.feature-block p:last-child{margin-bottom:0}.feature-block .icon{width:48px;height:48px}.common-FlagIcon:before{content:"";display:inline-block;background-image:url("/img/v3/common/flagIcons.svg?57");width:21px;height:15px;margin-right:12px;vertical-align:-2px}.common-FlagIcon--ad:before{background-position:-10px -10px}.common-FlagIcon--ae:before{background-position:-41px -10px}.common-FlagIcon--ag:before{background-position:-72px -10px}.common-FlagIcon--am:before{background-position:-103px -10px}.common-FlagIcon--ar:before{background-position:-134px -10px}.common-FlagIcon--at:before{background-position:-165px -10px}.common-FlagIcon--au:before{background-position:-196px -10px}.common-FlagIcon--be:before{background-position:-227px -10px}.common-FlagIcon--bf:before{background-position:-258px -10px}.common-FlagIcon--bg:before{background-position:-289px -10px}.common-FlagIcon--bo:before{background-position:-320px -10px}.common-FlagIcon--br:before{background-position:-351px -10px}.common-FlagIcon--ca:before{background-position:-382px -10px}.common-FlagIcon--cd:before{background-position:-413px -10px}.common-FlagIcon--cg:before{background-position:-444px -10px}.common-FlagIcon--ch:before{background-position:-475px -10px}.common-FlagIcon--cl:before{background-position:-506px -10px}.common-FlagIcon--cm:before{background-position:-10px -35px}.common-FlagIcon--cn:before{background-position:-41px -35px}.common-FlagIcon--co:before{background-position:-72px -35px}.common-FlagIcon--cr:before{background-position:-103px -35px}.common-FlagIcon--cz:before{background-position:-134px -35px}.common-FlagIcon--de:before{background-position:-165px -35px}.common-FlagIcon--dj:before{background-position:-196px -35px}.common-FlagIcon--dk:before{background-position:-227px -35px}.common-FlagIcon--dz:before{background-position:-258px -35px}.common-FlagIcon--ec:before{background-position:-289px -35px}.common-FlagIcon--ee:before{background-position:-320px -35px}.common-FlagIcon--eg:before{background-position:-351px -35px}.common-FlagIcon--es:before{background-position:-382px -35px}.common-FlagIcon--eu:before{background-position:-413px -35px}.common-FlagIcon--fi:before{background-position:-444px -35px}.common-FlagIcon--fo:before{background-position:-475px -35px}.common-FlagIcon--fr:before{background-position:-506px -35px}.common-FlagIcon--ga:before{background-position:-10px -60px}.common-FlagIcon--gb:before{background-position:-41px -60px}.common-FlagIcon--gl:before{background-position:-72px -60px}.common-FlagIcon--gm:before{background-position:-103px -60px}.common-FlagIcon--gr:before{background-position:-134px -60px}.common-FlagIcon--gt:before{background-position:-165px -60px}.common-FlagIcon--gu:before{background-position:-196px -60px}.common-FlagIcon--hk:before{background-position:-227px -60px}.common-FlagIcon--hn:before{background-position:-258px -60px}.common-FlagIcon--ht:before{background-position:-289px -60px}.common-FlagIcon--hu:before{background-position:-320px -60px}.common-FlagIcon--id:before{background-position:-351px -60px}.common-FlagIcon--ie:before{background-position:-382px -60px}.common-FlagIcon--il:before{background-position:-413px -60px}.common-FlagIcon--im:before{background-position:-444px -60px}.common-FlagIcon--in:before{background-position:-475px -60px}.common-FlagIcon--iq:before{background-position:-506px -60px}.common-FlagIcon--ir:before{background-position:-10px -85px}.common-FlagIcon--is:before{background-position:-41px -85px}.common-FlagIcon--it:before{background-position:-72px -85px}.common-FlagIcon--je:before{background-position:-103px -85px}.common-FlagIcon--jm:before{background-position:-134px -85px}.common-FlagIcon--jo:before{background-position:-165px -85px}.common-FlagIcon--jp:before{background-position:-196px -85px}.common-FlagIcon--kg:before{background-position:-227px -85px}.common-FlagIcon--kn:before{background-position:-258px -85px}.common-FlagIcon--kp:before{background-position:-289px -85px}.common-FlagIcon--kr:before{background-position:-320px -85px}.common-FlagIcon--kw:before{background-position:-351px -85px}.common-FlagIcon--kz:before{background-position:-382px -85px}.common-FlagIcon--la:before{background-position:-413px -85px}.common-FlagIcon--lb:before{background-position:-444px -85px}.common-FlagIcon--lc:before{background-position:-475px -85px}.common-FlagIcon--ls:before{background-position:-506px -85px}.common-FlagIcon--lt:before{background-position:-10px -110px}.common-FlagIcon--lu:before{background-position:-41px -110px}.common-FlagIcon--lv:before{background-position:-72px -110px}.common-FlagIcon--ma:before{background-position:-103px -110px}.common-FlagIcon--mg:before{background-position:-134px -110px}.common-FlagIcon--mk:before{background-position:-165px -110px}.common-FlagIcon--ml:before{background-position:-196px -110px}.common-FlagIcon--mm:before{background-position:-227px -110px}.common-FlagIcon--mt:before{background-position:-258px -110px}.common-FlagIcon--mx:before{background-position:-289px -110px}.common-FlagIcon--my:before{background-position:-320px -110px}.common-FlagIcon--na:before{background-position:-351px -110px}.common-FlagIcon--ne:before{background-position:-382px -110px}.common-FlagIcon--ng:before{background-position:-413px -110px}.common-FlagIcon--ni:before{background-position:-444px -110px}.common-FlagIcon--nl:before{background-position:-475px -110px}.common-FlagIcon--no:before{background-position:-506px -110px}.common-FlagIcon--nz:before{background-position:-10px -135px}.common-FlagIcon--om:before{background-position:-41px -135px}.common-FlagIcon--pa:before{background-position:-72px -135px}.common-FlagIcon--pe:before{background-position:-103px -135px}.common-FlagIcon--pg:before{background-position:-134px -135px}.common-FlagIcon--ph:before{background-position:-165px -135px}.common-FlagIcon--pk:before{background-position:-196px -135px}.common-FlagIcon--pl:before{background-position:-227px -135px}.common-FlagIcon--pr:before{background-position:-258px -135px}.common-FlagIcon--ps:before{background-position:-289px -135px}.common-FlagIcon--pt:before{background-position:-320px -135px}.common-FlagIcon--py:before{background-position:-351px -135px}.common-FlagIcon--qa:before{background-position:-382px -135px}.common-FlagIcon--ro:before{background-position:-413px -135px}.common-FlagIcon--ru:before{background-position:-444px -135px}.common-FlagIcon--rw:before{background-position:-475px -135px}.common-FlagIcon--sa:before{background-position:-506px -135px}.common-FlagIcon--se:before{background-position:-10px -160px}.common-FlagIcon--sg:before{background-position:-41px -160px}.common-FlagIcon--si:before{background-position:-72px -160px}.common-FlagIcon--sk:before{background-position:-103px -160px}.common-FlagIcon--sl:before{background-position:-134px -160px}.common-FlagIcon--sn:before{background-position:-165px -160px}.common-FlagIcon--so:before{background-position:-196px -160px}.common-FlagIcon--sv:before{background-position:-227px -160px}.common-FlagIcon--td:before{background-position:-258px -160px}.common-FlagIcon--th:before{background-position:-289px -160px}.common-FlagIcon--tj:before{background-position:-320px -160px}.common-FlagIcon--tl:before{background-position:-351px -160px}.common-FlagIcon--tr:before{background-position:-382px -160px}.common-FlagIcon--tw:before{background-position:-413px -160px}.common-FlagIcon--tz:before{background-position:-444px -160px}.common-FlagIcon--ua:before{background-position:-475px -160px}.common-FlagIcon--us:before{background-position:-506px -160px}.common-FlagIcon--uy:before{background-position:-10px -185px}.common-FlagIcon--ve:before{background-position:-41px -185px}.common-FlagIcon--vn:before{background-position:-72px -185px}.common-FlagIcon--xx:before{background-position:-103px -185px}.common-FlagIcon--ye:before{background-position:-134px -185px}.common-FlagIcon--za:before{background-position:-165px -185px}.globalNav{font-family:Camphor,Open Sans,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;position:absolute;left:0;top:10px;right:0;z-index:500;height:50px;-webkit-perspective:2000px;perspective:2000px}.globalNav ul{padding:0;margin:0}.globalNav li{list-style:none}.globalNav a{text-decoration:none;-webkit-tap-highlight-color:transparent;color:#6772e5;-webkit-transition:color .1s;transition:color .1s}.globalNav a:hover{color:#32325d}.globalNav>.container-lg{padding:0}.globalNav .navRoot{position:relative}.globalNav .navSection>a,.globalNav .navSection>button{outline:none}.keyboard-navigation .globalNav .navSection>a:not(.item-mobileMenu):focus>:before,.keyboard-navigation .globalNav .navSection>button:not(.item-mobileMenu):focus>:before{opacity:.75}.globalNav .navSection>a:not(.item-mobileMenu)>:before,.globalNav .navSection>button:not(.item-mobileMenu)>:before{content:"";position:absolute;left:-15px;right:-15px;top:5px;bottom:5px;-webkit-box-shadow:0 0 0 1.5px inset currentColor;box-shadow:inset 0 0 0 1.5px currentColor;border-radius:4px;opacity:0;-webkit-transition:opacity .15s;transition:opacity .15s}.globalNav .navSection.logo{position:absolute;top:0;left:0}.globalNav .navSection.primary,.globalNav .navSection.secondary{display:none}@media (min-width:670px){.globalNav .navSection.primary,.globalNav .navSection.secondary{display:-webkit-box;display:-ms-flexbox;display:flex}}.globalNav .navSection.primary{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.globalNav .navSection.secondary{position:absolute;top:0;right:0}.globalNav .navSection.mobile{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}@media (min-width:670px){.globalNav .navSection.mobile{display:none}}.globalNav.compact .navRoot{display:-webkit-box;display:-ms-flexbox;display:flex}.globalNav.compact .navSection.logo{position:static;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}.globalNav.compact .navSection.secondary{position:static}.globalNav .rootLink{display:inline-block;height:50px;white-space:nowrap;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;font-size:17px;line-height:50px;font-weight:400;margin:0;padding:0 10px}@media (min-width:670px){.globalNav .rootLink{padding:0 calc(-17.16247px + 4.0541vw);padding:0 calc(10px + (100vw - 670px) * .040541)}}@media (min-width:1040px){.globalNav .rootLink{padding:0 25px}}.globalNav .rootLink>*{position:relative;display:block}.globalNav .navSection.logo .rootLink{padding-left:20px!important}.globalNav .navSection.secondary .rootLink:last-child{padding-right:20px!important}.globalNav .navSection.primary .rootLink{font-weight:500}.globalNav .colorize{color:#6772e5;-webkit-transition:color .1s ease;transition:color .1s ease}.globalNav .colorize.active,.globalNav .colorize:hover{color:#32325d}.globalNav .hasDropdown{cursor:default}.globalNav .item-home h1{line-height:50px;font-size:20px;margin:0;color:inherit}.globalNav .item-home svg{vertical-align:-5px}.globalNav .item-home svg path{fill:currentColor}.globalNav .item-dashboard>span:after{font:normal 16px StripeIcons;content:"\279E";padding-left:6px}.globalNav .dropdownRoot{position:absolute;z-index:1000;left:0;right:0;top:50px;pointer-events:none;-webkit-transform:rotateX(-15deg);transform:rotateX(-15deg);-webkit-transform-origin:50% -50px;transform-origin:50% -50px;opacity:0;will-change:transform,opacity;-webkit-transition-property:opacity,-webkit-transform;transition-property:opacity,-webkit-transform;transition-property:transform,opacity;transition-property:transform,opacity,-webkit-transform;-webkit-transition-duration:.25s;transition-duration:.25s;display:none}@media (min-width:670px){.globalNav.initialized .dropdownRoot{display:block}}.globalNav.dropdownActive .dropdownRoot{opacity:1;pointer-events:auto;-webkit-transform:none;transform:none}.globalNav .dropdownBackground{background:#fff;border-radius:4px;overflow:hidden;-webkit-box-shadow:0 50px 100px -20px rgba(50,50,93,.25),0 30px 60px -30px rgba(0,0,0,.3);box-shadow:0 50px 100px -20px rgba(50,50,93,.25),0 30px 60px -30px rgba(0,0,0,.3);width:380px;height:400px;-webkit-transform:translateX(0);transform:translateX(0);-webkit-transform-origin:0 0;transform-origin:0 0}.globalNav .alternateBackground,.globalNav .dropdownBackground{position:absolute;top:0;left:0;will-change:transform;-webkit-transition-property:-webkit-transform;transition-property:-webkit-transform;transition-property:transform;transition-property:transform,-webkit-transform;-webkit-transition-duration:.25s;transition-duration:.25s}.globalNav .alternateBackground{right:0;height:1000px;background:#f6f9fc}.globalNav .dropdownArrow{top:-6px;margin:0 0 0 -6px;width:12px;height:12px;-webkit-transform:rotate(45deg);transform:rotate(45deg);border-radius:4px 0 0 0;background:#fff;-webkit-box-shadow:-3px -3px 5px rgba(82,95,127,.04);box-shadow:-3px -3px 5px rgba(82,95,127,.04);will-change:transform;-webkit-transition-property:-webkit-transform;transition-property:-webkit-transform;transition-property:transform;transition-property:transform,-webkit-transform}.globalNav .dropdownArrow,.globalNav .dropdownContainer{position:absolute;left:0;-webkit-transition-duration:.25s;transition-duration:.25s}.globalNav .dropdownContainer{overflow:hidden;width:500px;top:0;-webkit-transform:translateX(0);transform:translateX(0);will-change:transform,width,height;-webkit-transition-property:width,height,-webkit-transform;transition-property:width,height,-webkit-transform;transition-property:transform,width,height;transition-property:transform,width,height,-webkit-transform}.globalNav .dropdownSection{opacity:0;pointer-events:none;will-change:transform,opacity;-webkit-transition-property:opacity,-webkit-transform;transition-property:opacity,-webkit-transform;transition-property:transform,opacity;transition-property:transform,opacity,-webkit-transform;-webkit-transition-duration:.25s;transition-duration:.25s;background:red}.globalNav .dropdownSection.active{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}.globalNav .dropdownSection.left{-webkit-transform:translateX(-150px);transform:translateX(-150px)}.globalNav .dropdownSection.right{-webkit-transform:translateX(150px);transform:translateX(150px)}.globalNav.dropdownActive .dropdownSection.active{pointer-events:auto}.globalNav.noDropdownTransition .alternateBackground,.globalNav.noDropdownTransition .dropdownArrow,.globalNav.noDropdownTransition .dropdownBackground,.globalNav.noDropdownTransition .dropdownContainer,.globalNav.noDropdownTransition .dropdownSection{-webkit-transition:none;transition:none}.globalNav .dropdownContent{position:absolute;top:0;left:0}.globalNav .linkGroup{padding:20px 35px}.globalNav .linkContainer{display:block;padding:9px 0;outline:none;position:relative}.keyboard-navigation .globalNav .linkContainer:focus:before{opacity:.5}.globalNav .linkContainer:before{content:"";position:absolute;left:-10px;top:0;right:-10px;bottom:0;-webkit-box-shadow:0 0 0 1.5px #8898aa;box-shadow:0 0 0 1.5px #8898aa;border-radius:4px;opacity:0;-webkit-transition:opacity .15s;transition:opacity .15s}.globalNav .linkTitle{margin:0;color:#6772e5;font-size:16px;line-height:22px;text-transform:uppercase;font-weight:600;letter-spacing:.025em}.globalNav .linkSub{font-size:15px;line-height:22px;color:#6b7c93;margin:5px 0 0;display:block;white-space:nowrap}.globalNav .linkSub,.globalNav .linkTitle{-webkit-transition:color .1s;transition:color .1s}.globalNav .linkContainer:focus .linkTitle,.globalNav .linkContainer:hover .linkTitle,.globalNav .linkTitle:focus,.globalNav .linkTitle:hover{color:#32325d}.globalNav .linkContainer:focus .linkSub,.globalNav .linkContainer:hover .linkSub{color:#424770}.globalNav .hover-fillDark,.globalNav .hover-fillLight{-webkit-transition:fill .1s;transition:fill .1s}.globalNav .hover-strokeDark,.globalNav .hover-strokeLight{-webkit-transition:stroke .1s;transition:stroke .1s}.globalNav .linkContainer:focus .hover-fillLight,.globalNav .linkContainer:hover .hover-fillLight{fill:#8898aa}.globalNav .linkContainer:focus .hover-fillDark,.globalNav .linkContainer:hover .hover-fillDark{fill:#32325d}.globalNav .linkContainer:focus .hover-strokeLight,.globalNav .linkContainer:hover .hover-strokeLight{stroke:#8898aa}.globalNav .linkContainer:focus .hover-strokeDark,.globalNav .linkContainer:hover .hover-strokeDark{stroke:#32325d}.globalNav .linkIcon{white-space:nowrap}.globalNav .linkIcon svg{margin:0 12px -3px -1px}.globalNav .withIcon{padding-left:28px}.globalNav .withIcon .linkTitle{margin-left:-28px}.globalNav .new-badge{display:inline-block;margin-left:5px;vertical-align:2px;color:#fff;text-transform:uppercase;font-size:10px;line-height:1;font-weight:700;background:#6772e5;-webkit-transition:background .15s;transition:background .15s;border-radius:10px;padding:2px 4px 1px;height:auto;top:auto;-webkit-box-shadow:none;box-shadow:none}.globalNav .linkContainer:focus .new-badge,.globalNav .linkContainer:hover .new-badge{background:#32325d}.globalNav .productsGroupPrimary,.globalNav .productsGroupSecondary{margin:-5px -10px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.globalNav .productsGroupPrimary>li,.globalNav .productsGroupSecondary>li{-webkit-box-flex:1;-ms-flex:1 0 auto;flex:1 0 auto;display:-webkit-box;display:-ms-flexbox;display:flex}.globalNav .productsGroupPrimary .linkContainer,.globalNav .productsGroupSecondary .linkContainer{-webkit-box-flex:1;-ms-flex:1;flex:1;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.globalNav .productsGroupPrimary .linkContainer{padding:16px 8px}.globalNav .productsGroupPrimary svg{width:48px;height:48px}.globalNav .productsGroupPrimary .productLinkContent{-webkit-box-flex:1;-ms-flex:1;flex:1;margin-left:18px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.globalNav .productsGroupSecondary .linkContainer{padding:14px 8px 14px 12px}.globalNav .productsGroupSecondary svg{width:22px;height:22px}.globalNav .productsGroupSecondary .productLinkContent{-webkit-box-flex:1;-ms-flex:1;flex:1;margin-left:15px}.globalNav .productsGroupSecondary .linkTitle{display:inline}.globalNav .productsGroupSecondary .linkSub{display:inline;margin:0 0 0 10px}.globalNav .prodsubGroup{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;border-top:2px solid #fff}.globalNav .prodsubGroup .linkContainer{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;padding:13px 26px}.globalNav .prodsubGroup .linkSub{margin:0 0 0 10px}.globalNav .item-subscriptions .linkTitle{color:#24b47e}.globalNav .item-connect .linkTitle{color:#3297d3}.globalNav .item-sigma .linkTitle{color:#8f6ed5}.globalNav .item-connect .new-badge{background:#3297d3}.globalNav .item-relay .linkTitle{color:#e25950}.globalNav .item-atlas .linkTitle{color:#e39f48}.globalNav .item-radar .linkTitle{color:#b76ac4}.globalNav .item-sigma .new-badge{background:#8f6ed5}.globalNav .item-billing .new-badge,.globalNav .item-subscriptions .new-badge{background:#24b47e}.globalNav .documentationGroup .linkSub{max-width:400px}.globalNav .documentationArticles{font-size:15px;line-height:26px;margin:15px 20px 10px 28px;display:-webkit-box;display:-ms-flexbox;display:flex;white-space:nowrap}.globalNav .documentationArticles>ul{margin-right:40px}.globalNav .documentationArticles>ul:last-child{margin-right:0}.globalNav .documentationArticles h4{font-size:14px;line-height:22px;font-weight:500;text-transform:uppercase;letter-spacing:.025em;margin:0 0 3px;color:#8898aa}.globalNav .documentationArticles a{outline:none}.keyboard-navigation .globalNav .documentationArticles a:focus{color:#32325d;text-decoration:underline;text-underline-position:under}.globalNav .blogPosts{margin:5px 10px 5px 28px}.globalNav .blogPosts a{display:block;white-space:nowrap;padding:5px 0}.globalNav .blogPosts a:after{content:"\27A2";font:normal 16px StripeIcons;margin-left:6px;vertical-align:-3px}.globalNav .blogPosts .title{font-size:15px;line-height:22px;display:inline-block;white-space:nowrap;max-width:300px;text-overflow:ellipsis;overflow:hidden;vertical-align:top}.globalNav .blogPosts .title.new{font-weight:500}.globalNav .blogPosts a{outline:none}.keyboard-navigation .globalNav .blogPosts a:focus .title{color:#32325d;text-decoration:underline;text-underline-position:under}.globalNav .blogPosts .new-badge{vertical-align:-1px}.globalNav .blogPosts a:hover .new-badge. .globalNav .blogPosts a:focus .new-badge{background:#32325d}.globalNav .item-blog svg{-webkit-transform:translateX(3px);transform:translateX(3px)}.globalNav .navSection.mobile .rootLink{cursor:pointer;width:50px;height:50px;position:relative;padding:0 30px}.globalNav .navSection.mobile .rootLink h2{color:inherit}.globalNav .navSection.mobile .rootLink h2,.globalNav .navSection.mobile .rootLink h2:after,.globalNav .navSection.mobile .rootLink h2:before{position:absolute;width:24px;height:3px;border-radius:1px;background:currentColor}.globalNav .navSection.mobile .rootLink h2{font-size:0;left:13px;top:23px}.globalNav .navSection.mobile .rootLink h2:after,.globalNav .navSection.mobile .rootLink h2:before{content:"";left:0}.globalNav .navSection.mobile .rootLink h2:before{top:-9px}.globalNav .navSection.mobile .rootLink h2:after{top:9px}.globalNav .popup{position:absolute;left:10px;top:5px;right:10px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end;pointer-events:none;-webkit-perspective:2000px;perspective:2000px}.globalNav .popupContainer{background:#fff;-webkit-box-shadow:0 50px 100px -20px rgba(50,50,93,.25),0 30px 60px -30px rgba(0,0,0,.3);box-shadow:0 50px 100px -20px rgba(50,50,93,.25),0 30px 60px -30px rgba(0,0,0,.3);border-radius:4px;overflow:hidden;position:relative;font-size:17px;line-height:40px;white-space:nowrap;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-transform:scale(.95);transform:scale(.95);-webkit-transform-origin:100% 0;transform-origin:100% 0;opacity:0;will-change:transform,opacity;-webkit-transition-property:opacity,-webkit-transform;transition-property:opacity,-webkit-transform;transition-property:transform,opacity;transition-property:transform,opacity,-webkit-transform;-webkit-transition-duration:.25s;transition-duration:.25s}.globalNav .navSection.mobile.globalPopupActive .popupContainer{-webkit-transform:none;transform:none;opacity:1;pointer-events:auto}.globalNav .popup a{display:block}.globalNav .popupCloseButton{position:absolute;right:0;top:0;width:51px;height:51px;font-size:0;cursor:pointer}.globalNav .popupCloseButton:after,.globalNav .popupCloseButton:before{content:"";position:absolute;background:#6772e5;border-radius:1px;left:14px;right:14px;top:24px;height:3px;-webkit-transform:rotate(45deg);transform:rotate(45deg);-webkit-transition:background .1s;transition:background .1s}.globalNav .popupCloseButton:after{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.globalNav .popupCloseButton:hover:after,.globalNav .popupCloseButton:hover:before{background:#32325d}.globalNav .mobileSignIn{background:#f6f9fc;display:block;padding:12px 30px;font-weight:600}.globalNav .mobileSignIn:after{font:normal 16px StripeIcons;content:"\279C";margin-left:6px}.globalNav .mobileProducts{padding:20px 0 15px}.globalNav .mobileProducts h4{font-size:14px;font-weight:600;letter-spacing:.025em;color:#8898aa;text-transform:uppercase;margin:-5px 0 0 26px}.globalNav .mobileProductsList{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}.globalNav .mobileProductsList>ul{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}.globalNav .mobileProductsList>ul:last-child{-webkit-box-flex:3;-ms-flex-positive:3;flex-grow:3}.globalNav .mobileProductsList a{padding:0 26px;font-size:19px;font-weight:500;line-height:50px}.globalNav .mobileProductsList a:hover{color:#32325d}.globalNav .mobileProductsList a svg{display:inline-block;width:26px;height:26px;margin:0 10px 0 -3px;vertical-align:-6px}.globalNav .mobileProductsList .item-subscriptions{color:#24b47e}.globalNav .mobileProductsList .item-connect{color:#3297d3}.globalNav .mobileProductsList .item-relay{color:#e25950}.globalNav .mobileProductsList .item-sigma{color:#8f6ed5}.globalNav .mobileProductsList .item-atlas{color:#e39f48}.globalNav .mobileProductsList .item-radar{color:#b76ac4}.globalNav .mobileProductsList .new-badge{vertical-align:3px;margin-left:2px}.globalNav .mobileSecondaryNav{border-top:2px solid #f6f9fc;padding:15px 10px;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}.globalNav .mobileSecondaryNav>ul{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}.globalNav .mobileSecondaryNav>ul:last-child{-webkit-box-flex:3;-ms-flex-positive:3;flex-grow:3}.globalNav .mobileSecondaryNav a{padding:0 20px;min-width:100px}.globalNav .navSection.secondary.topNavCta--active{display:none}.globalNav .rootLink.topNavCta--variant0,.globalNav .rootLink.topNavCta--variant1,.globalNav .rootLink.topNavCta--variant2,.globalNav .rootLink.topNavCta--variant3,.globalNav .rootLink.topNavCta--variant4{letter-spacing:.025em}.globalNav .rootLink.topNavCta--variant0:hover{color:hsla(0,0%,100%,.8)}.globalNav .rootLink.topNavCta--variant1,.globalNav .rootLink.topNavCta--variant2{border:1px solid #fff;border-radius:4px;padding-left:20px;height:40px;line-height:36px;margin-top:6px}.globalNav .rootLink.topNavCta--variant1:hover,.globalNav .rootLink.topNavCta--variant2:hover{color:hsla(0,0%,100%,.8);border:1px solid hsla(0,0%,100%,.8)}.globalNav .rootLink.topNavCta--variant2{text-transform:uppercase;font-weight:600}.globalNav .rootLink.topNavCta--variant3,.globalNav .rootLink.topNavCta--variant4{text-transform:uppercase;text-shadow:0 1px 3px rgba(36,180,126,.4);border-radius:4px;font-size:16px;font-weight:600;padding:0 20px;height:40px;line-height:41px;margin-top:5px;-webkit-box-shadow:0 4px 6px rgba(50,50,93,.11),0 1px 3px rgba(0,0,0,.08);box-shadow:0 4px 6px rgba(50,50,93,.11),0 1px 3px rgba(0,0,0,.08);-webkit-transition:all .15s ease;transition:all .15s ease}.globalNav .rootLink.topNavCta--variant3{background:#4c3df5}.globalNav .rootLink.topNavCta--variant4{background:#32325d}.globalNav .rootLink.topNavCta--variant3:hover,.globalNav .rootLink.topNavCta--variant4:hover{-webkit-transform:translateY(-1px);transform:translateY(-1px);-webkit-box-shadow:0 7px 14px rgba(50,50,93,.1),0 3px 6px rgba(0,0,0,.08);box-shadow:0 7px 14px rgba(50,50,93,.1),0 3px 6px rgba(0,0,0,.08);text-shadow:none;color:#fff}@media (min-width:1040px){.globalNav.topNavCta--active .rootLink{padding:0 20px}}.productNav{font-family:Camphor,Open Sans,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;position:absolute;left:0;top:70px;right:0;z-index:499;font-size:15px;font-weight:600;letter-spacing:.025em;text-transform:uppercase;padding:12px 0}.productNav>.container-lg{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;position:relative}.productNav .separator{position:absolute;width:calc(100% - 40px);height:2px;top:-17px;background-color:currentColor;opacity:.07;pointer-events:none}.productNav a.home{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.productNav a.home svg{display:block;width:30px;height:30px}.productNav a.home span{margin-left:12px}.productNav .mask-container{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end;margin:0 -20px 0 20px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 20px,#000 calc(100% - 20px),transparent)}.productNav .mask-container,.productNav ul{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.productNav ul{padding:0 0 10px;margin-bottom:-10px;overflow:auto;line-height:30px;-webkit-overflow-scrolling:touch;-webkit-mask-image:linear-gradient(180deg,#000,#000 calc(100% - 10px),transparent calc(100% - 10px),transparent)}.productNav ul::-webkit-scrollbar{display:none}.productNav li{list-style:none;padding:0 10px}.productNav li:first-child{padding-left:20px}.productNav li:last-child{padding-right:20px}@media (min-width:420px){.productNav li{padding:0 15px}}@media (min-width:670px){.productNav li{padding:0 20px}}.productNav a{text-decoration:none;-webkit-tap-highlight-color:transparent;color:#6772e5;-webkit-transition:color .1s;transition:color .1s;white-space:nowrap}.keyboard-navigation .productNav a:focus{outline:none;text-decoration:underline;text-underline-position:under}.productNav a:hover{color:#32325d}.productNav a.external:after{font:normal 14px StripeIcons;content:"\279C";padding-left:5px}.productNav .colorize{color:#6772e5;-webkit-transition:color .1s ease;transition:color .1s ease}.productNav .colorize.active,.productNav .colorize:hover{color:#32325d}html[lang=ja] .productNav ul{white-space:nowrap}.globalFooter{font-family:Camphor,Open Sans,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;background:#f6f9fc;position:relative}.globalFooter.withCards{background:transparent;overflow:hidden;padding-top:500px;margin-top:-480px;pointer-events:none}.globalFooter.withCards>*{pointer-events:auto;position:relative}.globalFooter.withCards:before{content:"";position:absolute;left:0;right:0;top:600px;height:2000px;background:#f6f9fc;-webkit-transform:skew(0,-12deg);transform:skew(0,-12deg)}.globalFooterCards .container-lg,.globalFooterCards .container-xl{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin:-15px auto;padding:0 5px}a.globalFooterCard,div.globalFooterCard{-webkit-box-flex:1;-ms-flex:1 1 100%;flex:1 1 100%;margin:15px;z-index:499;position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;overflow:hidden;padding:40px 40px 40px 120px;background-color:#fff;border-radius:8px;-webkit-box-shadow:0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);box-shadow:0 13px 27px -5px rgba(50,50,93,.25),0 8px 16px -8px rgba(0,0,0,.3);-webkit-transition-property:color,background-color,-webkit-box-shadow,-webkit-transform;transition-property:color,background-color,-webkit-box-shadow,-webkit-transform;transition-property:color,background-color,box-shadow,transform;transition-property:color,background-color,box-shadow,transform,-webkit-box-shadow,-webkit-transform;-webkit-transition-duration:.15s;transition-duration:.15s}a.globalFooterCard:after,div.globalFooterCard:after{content:"";position:absolute;left:0;top:0;right:0;bottom:0;background:#aab7c4;pointer-events:none;opacity:0;-webkit-transition:opacity .15s;transition:opacity .15s}@media (min-width:670px){a.globalFooterCard,div.globalFooterCard{-ms-flex-preferred-size:1%;flex-basis:1%;padding-left:100px}}@media (min-width:880px){a.globalFooterCard,div.globalFooterCard{padding-left:120px}}a.globalFooterCard:hover,div.globalFooterCard:hover{color:#32325d!important;-webkit-transform:translateY(-2px);transform:translateY(-2px)}a.globalFooterCard:active,a.globalFooterCard:hover,div.globalFooterCard:active,div.globalFooterCard:hover{-webkit-box-shadow:0 30px 60px -12px rgba(50,50,93,.25),0 18px 36px -18px rgba(0,0,0,.3);box-shadow:0 30px 60px -12px rgba(50,50,93,.25),0 18px 36px -18px rgba(0,0,0,.3)}a.globalFooterCard:active,div.globalFooterCard:active{-webkit-transform:translateY(2px);transform:translateY(2px)}a.globalFooterCard:active:after,div.globalFooterCard:active:after{opacity:.15}a.globalFooterCard img,a.globalFooterCard svg,div.globalFooterCard img,div.globalFooterCard svg{position:absolute;width:130px;height:130px;left:-35px;top:calc(50% - 65px)}@media (min-width:670px){a.globalFooterCard img,a.globalFooterCard svg,div.globalFooterCard img,div.globalFooterCard svg{left:-50px}}@media (min-width:880px){a.globalFooterCard img,a.globalFooterCard svg,div.globalFooterCard img,div.globalFooterCard svg{left:-35px}}a.globalFooterCard svg .hover-fillDark,a.globalFooterCard svg .hover-fillLight,a.globalFooterCard svg .hover-fillMedium,div.globalFooterCard svg .hover-fillDark,div.globalFooterCard svg .hover-fillLight,div.globalFooterCard svg .hover-fillMedium{-webkit-transition:fill .15s;transition:fill .15s}a.globalFooterCard svg .hover-strokeDark,a.globalFooterCard svg .hover-strokeLight,div.globalFooterCard svg .hover-strokeDark,div.globalFooterCard svg .hover-strokeLight{-webkit-transition:stroke .15s;transition:stroke .15s}a.globalFooterCard:hover svg .hover-fillDark,div.globalFooterCard:hover svg .hover-fillDark{fill:#32325d}a.globalFooterCard:hover svg .hover-fillMedium,div.globalFooterCard:hover svg .hover-fillMedium{fill:#525f7f}a.globalFooterCard:hover svg .hover-fillLight,div.globalFooterCard:hover svg .hover-fillLight{fill:#8898aa}a.globalFooterCard:hover svg .hover-strokeDark,div.globalFooterCard:hover svg .hover-strokeDark{stroke:#32325d}a.globalFooterCard:hover svg .hover-strokeLight,div.globalFooterCard:hover svg .hover-strokeLight{stroke:#8898aa}a.globalFooterCard h2,div.globalFooterCard h2{margin:0 0 5px;white-space:normal}a.globalFooterCard p,div.globalFooterCard p{margin:5px 0 0}a.globalFooterCard.card-pricing,div.globalFooterCard.card-pricing{color:#24b47e}a.globalFooterCard.card-documentation,div.globalFooterCard.card-documentation{color:#b76ac4}a.globalFooterCard.card-subscriptions,div.globalFooterCard.card-subscriptions{color:#24b47e}a.globalFooterCard.card-connect,div.globalFooterCard.card-connect{color:#3297d3}a.globalFooterCard.card-relay,div.globalFooterCard.card-relay{color:#e25950}a.globalFooterCard.card-atlas,div.globalFooterCard.card-atlas{color:#e39f48}a.globalFooterCard.card-radar,div.globalFooterCard.card-radar{color:#b76ac4}a.globalFooterCard.card-sigma,div.globalFooterCard.card-sigma{color:#8f6ed5}a.globalFooterCard.card-jobs,div.globalFooterCard.card-jobs{color:#6772e5}a.globalFooterCard.card-environment,div.globalFooterCard.card-environment{color:#24b47e}.globalFooterCTA{padding:50px 0;border-bottom:2px solid rgba(207,215,223,.25)}@media (min-width:670px){.globalFooterCTA .container-lg{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}}.globalFooterCTA .buttons,.globalFooterCTA .content{-webkit-box-flex:1;-ms-flex:1 0 50%;flex:1 0 50%}.globalFooterCTA .title{font-weight:400;font-size:30px;line-height:45px;color:#32325d;margin:.75em 0}.globalFooterCTA .subtitle{font-weight:300;color:#6772e5;display:block}@media (min-width:670px){.globalFooterCTA .common-ButtonGroup{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}}.globalFooterCTA--collect{padding-top:calc(50px + .75em)}.globalFooterCTA--collect .content{margin:0 0 20px}@media(min-width:670px){.globalFooterCTA--collect .content{margin:0}}.globalFooterCTA--collect .title{margin:0;color:#32325d}.globalFooterCTA--collect .collect-email-partial{width:100%;max-width:400px;position:relative}.globalFooterCTA--collect .collect-email{-webkit-box-flex:1;-ms-flex:1 0 50%;flex:1 0 50%;margin:0}@media (min-width:670px){.globalFooterCTA--collect .collect-email{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}}.globalFooterCTA--collect .collect-input{background:#fff;-webkit-box-shadow:0 2px 5px -1px rgba(50,50,93,.25),0 1px 3px -1px rgba(0,0,0,.3);box-shadow:0 2px 5px -1px rgba(50,50,93,.25),0 1px 3px -1px rgba(0,0,0,.3);border-radius:4px;overflow:hidden;font-size:16px;line-height:22px;color:#32325d;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:-webkit-box-shadow .15s ease;transition:-webkit-box-shadow .15s ease;transition:box-shadow .15s ease;transition:box-shadow .15s ease,-webkit-box-shadow .15s ease}.globalFooterCTA--collect .collect-input.active{-webkit-box-shadow:0 6px 12px -2px rgba(50,50,93,.25),0 3px 7px -3px rgba(0,0,0,.3);box-shadow:0 6px 12px -2px rgba(50,50,93,.25),0 3px 7px -3px rgba(0,0,0,.3)}.globalFooterCTA--collect .collect-input .email-field{-webkit-box-flex:1;-ms-flex:1;flex:1;width:50%}.globalFooterCTA--collect .collect-input .submit-button{margin:0;border:none;outline:none;background:transparent;padding:9px 13px;font:inherit;font-size:15px;text-transform:uppercase;font-weight:600;letter-spacing:.025em;color:#6772e5;cursor:pointer;position:relative;-webkit-transition:all .15s ease;transition:all .15s ease;padding-left:15px}.globalFooterCTA--collect .collect-input .submit-button:before{content:"";position:absolute;left:0;top:7px;bottom:7px;width:2px;background:#f6f9fc}.globalFooterCTA--collect .collect-input .submit-button:focus{background-color:#f6f9fc}.globalFooterCTA--collect .collect-input .submit-button:hover{color:#7795f8}.globalFooterCTA--collect .collect-input .submit-button:active{color:#555abf;background-color:#f6f9fc}.globalFooterCTA--collect .collect-input input[type=email]{border:none;outline:none;margin:0;padding:9px 13px;background:transparent;font:inherit;color:#32325d}.globalFooterCTA--collect .collect-input input[type=email]::-webkit-input-placeholder{color:#aab7c4}.globalFooterCTA--collect .collect-input input[type=email]::-moz-placeholder{color:#aab7c4}.globalFooterCTA--collect .collect-input input[type=email]:-ms-input-placeholder{color:#aab7c4}.globalFooterCTA--collect .collect-error{width:100%;text-align:center;font:400 15px Camphor;color:#6b7c93;position:absolute;right:0;top:100%;-webkit-transform:translateY(10px);transform:translateY(10px);display:none}@media(min-width:670px){.globalFooterCTA--collect .collect-error{text-align:right}}.globalFooterCTA--collect .collect-success{-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start;display:none}@media(min-width:670px){.globalFooterCTA--collect .collect-success{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end;padding-right:80px}}.globalFooterCTA--collect .collect-success img{width:22px;height:22px;margin:0 10px 0 0}.globalFooterCTA--collect .collect-success span{font-weight:500}.globalFooterNav{padding:65px 0 55px;color:#8898aa;line-height:30px;font-size:15px;white-space:nowrap}.globalFooterNav ul{padding:0;margin:0}.globalFooterNav li{list-style:none}.globalFooterNav .container-lg{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}@media (min-width:880px){.globalFooterNav .container-lg{-ms-flex-wrap:nowrap;flex-wrap:nowrap}}.globalFooterNav a{text-decoration:none;color:inherit;-webkit-transition:color .1s;transition:color .1s}.globalFooterNav a:hover{color:#32325d}.globalFooterNav .metaNav{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-webkit-box-flex:2;-ms-flex-positive:2;flex-grow:2;-ms-flex-preferred-size:100%;flex-basis:100%;margin-bottom:20px}@media (min-width:880px){.globalFooterNav .metaNav{-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;margin:0 0 20px}}.globalFooterNav .metaNav>li{margin-right:20px}.globalFooterNav .metaNav .select{position:relative;-webkit-perspective:2000px;perspective:2000px;z-index:499}.globalFooterNav .metaNav .rootLink{color:#6772e5;font-weight:600;cursor:pointer}.globalFooterNav .metaNav .rootLink:hover{color:#32325d}.globalFooterNav .metaNav .rootLink svg{display:inline-block;vertical-align:-1px;margin:0 7px 0 -2px}.globalFooterNav .metaNav .rootLink svg path{fill:currentColor}.globalFooterNav .metaNav .select.globalPopupActive .rootLink{color:#32325d}@media (min-width:880px){.globalFooterNav .metaNav .country{margin-bottom:5px}}.globalFooterNav .metaNav .space{-webkit-box-flex:2;-ms-flex-positive:2;flex-grow:2}.globalFooterNav .metaNav .copyright{margin-right:0;color:#cfd7df}.globalFooterNav .siteNav{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}@media (min-width:670px){.globalFooterNav .siteNav{-ms-flex-wrap:nowrap;flex-wrap:nowrap}}@media (min-width:880px){.globalFooterNav .siteNav{-webkit-box-flex:0;-ms-flex-positive:0;flex-grow:0}}.globalFooterNav .siteNav .column{-ms-flex-preferred-size:50%;flex-basis:50%;margin-bottom:20px}@media (min-width:670px){.globalFooterNav .siteNav .column{-ms-flex-preferred-size:auto!important;flex-basis:auto!important;margin-right:40px}}@media (min-width:880px){.globalFooterNav .siteNav .column{margin-right:30px}}@media (min-width:1040px){.globalFooterNav .siteNav .column{margin-right:40px}}.globalFooterNav .siteNav .column:last-child{margin-right:0}.globalFooterNav .siteNav .splitColumn{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}.globalFooterNav .siteNav li{margin-right:40px}.globalFooterNav .siteNav li.long-link{margin-right:20px}.globalFooterNav .siteNav .column:last-child li{margin-right:0}.globalFooterNav .siteNav h4{font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.025em;margin:0 0 5px}.globalFooterNav .siteNav strong{font-weight:500}.globalFooterNav .popup{position:absolute;bottom:40px;left:-5px;z-index:1000;font-size:15px;line-height:26px;background:#fff;border-radius:4px;-webkit-box-shadow:0 50px 100px -20px rgba(50,50,93,.25),0 30px 60px -30px rgba(0,0,0,.3);box-shadow:0 50px 100px -20px rgba(50,50,93,.25),0 30px 60px -30px rgba(0,0,0,.3);pointer-events:none;-webkit-transform:rotate3d(1,1,0,15deg);transform:rotate3d(1,1,0,15deg);-webkit-transform-origin:0 100%;transform-origin:0 100%;opacity:0;will-change:transform,opacity;-webkit-transition-property:opacity,-webkit-transform;transition-property:opacity,-webkit-transform;transition-property:transform,opacity;transition-property:transform,opacity,-webkit-transform;-webkit-transition-duration:.25s;transition-duration:.25s}@media (min-width:1160px){.globalFooterNav .popup{left:-65px}}.globalFooterNav .popup:before{content:"";position:absolute;bottom:-6px;left:30px;width:20px;height:20px;-webkit-transform:rotate(45deg);transform:rotate(45deg);border-radius:20px 0 3px 0;background:#fff}@media (min-width:1160px){.globalFooterNav .popup:before{left:60px}}.globalFooterNav .globalPopupActive{z-index:1000!important}.globalFooterNav .globalPopupActive .popup{-webkit-transform:none;transform:none;opacity:1;pointer-events:auto}.globalFooterNav .optionList{color:#525f7f;white-space:nowrap}.globalFooterNav .optionList a{border-radius:4px;display:block;line-height:36px;padding:0 15px;-webkit-transition:color .1s,background-color .1s;transition:color .1s,background-color .1s}.globalFooterNav .optionList a:hover{background-color:#f6f9fc;color:#32325d}.globalFooterNav .optionList a:active{background-color:#e6ebf1}.globalFooterNav .optionList .selected{font-weight:600;color:#32325d}.globalFooterNav .optionList .selected>span:before{content:"";display:inline-block;width:14px;height:14px;vertical-align:-2px;margin:0 6px 0 -2px;background:url(/img/v3/common/footer/select/checkmark.svg);background-size:contain;background-repeat:no-repeat}.globalFooterNav .badge{font-size:10px;line-height:10px;color:#aab7c4;font-weight:600;text-transform:uppercase;letter-spacing:.025em;font-style:normal;padding:2px 3px 1px;border-radius:4px;border:1px solid #e6ebf1;display:inline-block;vertical-align:1px;margin-left:8px}.globalFooterNav .languagePicker{padding:10px 5px}.globalFooterNav .countryPicker{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;overflow:visible}.globalFooterNav .countryPicker:before{background:#f6f9fc}@media (min-width:670px){.globalFooterNav .countryPicker{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}.globalFooterNav .countryPicker:before{background:#fff}}.globalFooterNav .columns,.globalFooterNav .sidebar{display:-webkit-box;display:-ms-flexbox;display:flex}.globalFooterNav .sidebar{background:#f6f9fc;border-radius:0 0 5px 5px;overflow:visible;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.globalFooterNav .sidebar .countryList{background:#f6f9fc}@media (min-width:670px){.globalFooterNav .sidebar{border-radius:0 5px 5px 0}}.globalFooterNav .sidebar .optionList a:hover{background-color:rgba(230,235,241,.5)}.globalFooterNav .sidebar .optionList a:active{background-color:rgba(207,215,223,.5)}.globalFooterNav .countryList{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding:25px;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:calc(100vw - 40px);-webkit-overflow-scrolling:touch;background-color:#fff;overflow:visible}.globalFooterNav .countryList h4{margin:0 0 5px}.globalFooterNav .countryList h4 a{line-height:36px;padding:0 15px;text-transform:uppercase;color:#6772e5;font-size:14px;font-weight:600;letter-spacing:.025em}.globalFooterNav .countryList h4 a:hover{color:#32325d}.globalFooterNav .countryList h4 a:after{font:normal 16px StripeIcons;content:"\2192";margin-left:6px}.globalFooterNav .globalLink{border-top:2px solid #fff;padding:30px 40px}.globalFooterNav .globalLink:hover{color:#424770}.globalFooterNav .globalLink:hover strong{color:#32325d}.globalFooterNav .globalLink strong{display:block;color:#6772e5;font-weight:500;-webkit-transition:color .1s;transition:color .1s}.globalFooterNav .globalLink strong:after{font:normal 16px StripeIcons;content:"\2192";margin-left:6px}.cookie-notification-container{position:fixed;left:0;right:0;bottom:0;text-align:center;display:none;z-index:1100}@media (min-width:420px){.cookie-notification-container{bottom:10px}}.cookie-notification-container.shown{display:block}.cookie-notification-container.dismissed,.cookie-notification-container.shown.dismissed{display:none}.cookie-notification{background:rgba(246,249,252,.9);-webkit-box-shadow:0 6px 12px -2px rgba(50,50,93,.25),0 3px 7px -3px rgba(0,0,0,.3);box-shadow:0 6px 12px -2px rgba(50,50,93,.25),0 3px 7px -3px rgba(0,0,0,.3);font-size:15px;color:#424770;margin:0 auto;display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}@supports ((-webkit-backdrop-filter:blur(20px)) or (backdrop-filter:blur(20px))){.cookie-notification{background:rgba(246,249,252,.75);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}}@media (min-width:420px){.cookie-notification{border-radius:4px}}.cookie-notification .cookie-notification-copy{padding:8px 5px 8px 15px}.cookie-notification .dismiss-button{-webkit-appearance:none;-moz-appearance:none;appearance:none;background:transparent;border:none;outline:none;overflow:hidden;text-indent:-9999px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;position:relative;width:40px;height:40px;color:#8898aa;-webkit-transition:color .15s;transition:color .15s;cursor:pointer}.cookie-notification .dismiss-button:after,.cookie-notification .dismiss-button:before{content:"";position:absolute;left:50%;top:50%;width:40%;height:2px;background:currentColor;border-radius:2px;-webkit-transform:translate(-50%,-50%) rotate(45deg);transform:translate(-50%,-50%) rotate(45deg)}.cookie-notification .dismiss-button:after{-webkit-transform:translate(-50%,-50%) rotate(-45deg);transform:translate(-50%,-50%) rotate(-45deg)}.cookie-notification .dismiss-button:hover{color:#32325d} 

'''

js = '''

(function(m,n){function p(a){a=e[a].toString()+"%";dataLayer.push({event:"scroll-milestone",milestone:a})}dataLayer=window.dataLayer||[];var q=m,e=n,h=0,k,l=0,f=Math.max,r=Math.round;window.onscroll=function(){var a=window,b=document;var c=a.innerHeight||(b.documentElement?b.documentElement.clientHeight:b.body.clientHeight)||b.body.clientHeight;var d=b.body;var g=b.documentElement;d=b.height||f(f(d.scrollHeight,g.scrollHeight),f(d.offsetHeight,g.offsetHeight),f(d.clientHeight,g.clientHeight));a=a.pageYOffset||
(b.documentElement?b.documentElement.scrollTop:b.body.scrollTop)||b.body.scrollTop;c=d-(c+a);c=c/d*100;c=100-c;for(a=e.length;a;)a--,r(c)&gt;=e[a]&amp;&amp;l&lt;e[a]&amp;&amp;(currentMilestone=l=e[a],currentMilestone!=h&amp;&amp;(h=currentMilestone,window.clearTimeout(k),k=window.setTimeout(p(a),q)),a=0)}})(2E3,[0,25,50,75,100]);</script><script type="text/javascript" id="">ga(function(){var a=ga.getAll()[0].get("name");ga(a+".require","Clearbit",{mapping:{companyDomain:"dimension18",companyEmployeesRange:"dimension19",companyEstimatedAnnualRevenue:"dimension20"}})});

'''

import re

def beautyCSS( data ):

	data = re.sub(' +', ' ', data)
	data = data.replace(" :", ":").replace(";", ";\n")
	data = data.replace("}", "\n}\n\n")
	data = data.replace("{", "{\n")

	dataSplit = data.split("\n")

	counter = 0
	for i,line in enumerate(dataSplit):

		if "}" in line: counter = counter - 1
		dataSplit[i] = "\t"*counter + line
		if "{" in line: counter = counter + 1


	data = "\n".join( dataSplit )

	return data


def beautyJS( data ):
	return jsbeautifier.beautify( data )

def beautyHTML( data ):

	if type(data).__name__ == "str":
		soup = BeautifulSoup( data, 'html.parser')
	else:
		soup = data

	#-------------------------------------------
	#  Javascript
	#-------------------------------------------
	scripts = soup.findAll('script')
	for tag in scripts:
		data = beautyJS( tag.text )
		if len(data) > 5:
			data = "\n" + data
			data = data.replace("\n","\n\t\t")

			tag.string = "\n//Beautified\r\n\t"+data

	#-------------------------------------------
	#  CSS
	#-------------------------------------------
	styles = soup.findAll('style')
	for tag in styles:
		data = beautyCSS( tag.text )
		data = data.replace("\n","\n\t\t")

		tag.string = "\n/*Beautified*/\r\n\t"+data

	return soup.prettify()



#print(  repr(beautyCSS( css )) )
#print(  beautyCSS( css ) )
#print(  beautyHTML( code ) )

soup = BeautifulSoup( code, 'html.parser')
styles = soup.findAll('link')
for tag in styles:
	href = tag["href"]
	href = deleteFirst( "/", href )
	tag["href"] = href

print(soup.prettify())

