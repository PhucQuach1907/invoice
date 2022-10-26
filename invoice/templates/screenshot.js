document.querySelector('button').addEventListener('click', function () {
  html2canvas(document.querySelector('.specific'), {
    onrendered: function (canvas) {
      return Canvas2Image.saveAsPNG(canvas);
    },
  });
});
