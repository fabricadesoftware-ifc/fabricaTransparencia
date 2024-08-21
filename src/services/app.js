import api from "@/plugins/api";

class AppService {
    async getCharts() {
        try {
            const { data } = await api.get('/');
            return data.results;
        } catch (error) {
            console.log("error in get charts", error);
            throw error;
        }
    }
}

export default new AppService();