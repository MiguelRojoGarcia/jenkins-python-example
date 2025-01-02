from src.tools import get_system_resume

def test_get_system_resume():
    system_resumen = get_system_resume()
    assert system_resumen is not None
    assert "current_memory_usage" in system_resumen and system_resumen["current_memory_usage"] is not None
    assert "cpu_usage" in system_resumen and system_resumen["cpu_usage"] is not None
    assert False is True
    