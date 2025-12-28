document.addEventListener("DOMContentLoaded", function () {
    const brandSelect = document.getElementById("id_brand");
    const seriesSelect = document.getElementById("id_car_series");

    // Более надежная проверка элементов
    if (!brandSelect || !seriesSelect) {
        console.warn("Не найдены необходимые элементы select");
        return;
    }

    brandSelect.addEventListener("change", function () {
        const brandId = this.value.trim();

        // Сохраняем текущее состояние и блокируем выбор
        seriesSelect.innerHTML = '<option value="">---------</option>';
        seriesSelect.disabled = true;

        if (!brandId) {
            seriesSelect.disabled = false;
            return;
        }

        // Показываем индикатор загрузки
        const originalText = seriesSelect.querySelector('option')?.textContent || '---------';
        seriesSelect.innerHTML = `<option value="">Загрузка...</option>`;

        fetch(`/admin/parts/part/get-series/?brand_id=${encodeURIComponent(brandId)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                seriesSelect.innerHTML = '<option value="">---------</option>';

                if (data && data.length > 0) {
                    data.forEach(item => {
                        const option = document.createElement("option");
                        option.value = item.id;
                        option.textContent = item.name;
                        seriesSelect.appendChild(option);
                    });
                } else {
                    seriesSelect.innerHTML = '<option value="">Нет доступных серий</option>';
                }
            })
            .catch(err => {
                console.error("Ошибка загрузки серий:", err);
                seriesSelect.innerHTML = '<option value="">Ошибка загрузки</option>';
            })
            .finally(() => {
                seriesSelect.disabled = false;
            });
    });

    // Инициализация при загрузке, если бренд уже выбран
    if (brandSelect.value) {
        brandSelect.dispatchEvent(new Event('change'));
    }
});