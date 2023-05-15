// script.js

// Получаем ссылки на необходимые элементы формы
const orderForm = document.getElementById('order-form');
const orderPreview = document.getElementById('order-preview');
const orderDetails = document.getElementById('order-details');
const confirmButton = document.getElementById('confirm-button');
const newOrderButton = document.getElementById('new-order-button');

// Обработчик события отправки формы
orderForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Отменяем отправку формы

  // Получаем значения полей формы
  const manager = orderForm.elements['manager'].value;
  const lastName = orderForm.elements['last-name'].value;
  const firstName = orderForm.elements['first-name'].value;
  const middleName = orderForm.elements['middle-name'].value;
  const measurements = orderForm.elements['measurements'].value;
  const fabricType = orderForm.elements['fabric-type'].value;
  const deliveryOption = orderForm.elements['delivery-option'].value;

  // Формируем текст для предварительного просмотра заказа
  const orderText = `
    Менеджер: ${manager},
    Фамилия: ${lastName},
    Имя: ${firstName},
    Отчество: ${middleName},
    Измерения: ${measurements},
    Тип ткани: ${fabricType},
    Способ доставки: ${deliveryOption}
  `;

  // Отображаем предварительный просмотр заказа
  orderDetails.textContent = orderText;
  orderPreview.style.display = 'block';
});

// Обработчик события подтверждения заказа
confirmButton.addEventListener('click', function() {
  // Выводим данные заказа в консоль браузера
  alert(orderDetails.textContent)
  eel.processOrderDetails(orderDetails.textContent);

  // Скрываем форму и предварительный просмотр заказа
  orderForm.style.display = 'none';
  orderPreview.style.display = 'none';

  // Выводим сообщение об успешном создании заказа
  const successMessage = document.createElement('p');
  successMessage.textContent = 'Заказ успешно создан';
  document.body.appendChild(successMessage);

  // Создаем кнопку для нового заказа
  const newOrderButton = document.createElement('button');
  newOrderButton.textContent = 'Сделать новый заказ';
  newOrderButton.style.cssText = 'background-color: green; color: white; border: none; padding: 10px 20px;border-radius: 4px; cursor: pointer;';
  document.body.appendChild(newOrderButton);

  // Обработчик события для кнопки нового заказа
  newOrderButton.addEventListener('click', function() {
    // Перезагружаем страницу
    location.reload();
  });
});
