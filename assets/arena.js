function() {

  function adjustFooter() {
    const footer = document.getElementById('send-area');
    const modeScreen = document.getElementById('mode-screen');
    const chatArea = document.getElementById('chat-area');

    const footerHeight = footer.offsetHeight;
    // Add bottom padding to the chatArea equal to footer height so it's not hidden
    chatArea.style.paddingBottom = `${footerHeight}px`;
    modeScreen.style.paddingBottom = `${footerHeight}px`;
  }
  window.addEventListener('load', adjustFooter);
  window.addEventListener('resize', adjustFooter);
  window.addEventListener('click', adjustFooter);
  adjustFooter();

  console.log("Git commit: __GIT_COMMIT__");

  Sentry.onLoad(function () {
    Sentry.init({
      integrations: [
        // If you use a bundle with tracing enabled, add the BrowserTracing integration
        Sentry.browserTracingIntegration(),
        // If you use a bundle with session replay enabled, add the Replay integration
        Sentry.replayIntegration(),
      ],

      replaysSessionSampleRate: 0.1,
      replaysOnErrorSampleRate: 1.0,
      dsn: "https://454e45b18f4ad93227ac60659a7d373c@sentry.incubateur.net/164",
      environment: "Development",

      tracesSampleRate: 0.2
    });
  });

}


